import struct
from crysp.utils.operators import *


class Cipher:
    def __init__(self):
        self.__CONST_EXPAND = b"expand 32-byte k"
        self.__MAX_NUM = 0xFFFFFFFF
        self.__COUNTER_LENGTH = 64
    
    def __sum(self, a:int, b:int)->int:
        """Сложение двух чисел по модулю 2^32

        Args:
            a (int): Первое число
            b (int): Второе число

        Returns:
            int: Результат сложения
        """        
        res = a + b
        return res - self.__MAX_NUM if res >= self.__MAX_NUM else res

    def __setup_keystate(self, key: bytes, nonce: bytes, counter: int = 0):
        """Устанавливает начальное состояние ключа

        Args:
            key (bytes): Ключ, используемый для шифрования данных 32 байта
            nonce (bytes): Одноразовая номер, используемая для генерации keystate
            counter (int, optional): Определяет, какой блок шифруется. Defaults to 0.
        """
        nonce = list(struct.unpack("<2I", nonce))
        count = [counter >> 16, counter & 0xFFFF]
        const = list(struct.unpack("<4I", self.__CONST_EXPAND))
        k = list(struct.unpack("<8I", key))

        self.__state = [
            const[0], k[0],     k[1],     k[2],
            k[3],     const[1], nonce[0], nonce[1],
            count[1], count[0], const[2], k[4],
            k[5],     k[6],     k[7],     const[3]]
    
    def __rol(self, a:int, n:int)->int:
        """Циклический свдиг влево

        Args:
            a (int): Число для свдига
            n (int): Шаг сдвига

        Returns:
            int: Результат сдвига
        """        
        n = n % (len(str(a))*8)
        t1 = a << n
        t2 = a >> (len(str(a))*8 - n)
        return t1 | t2;  


    def __QR(self, x: list, a: int, b: int, c: int, d: int):
        """Функция четверти круга

        Args:
            x (list): Начальный массив для перестановки
            a (int): Значение индекса для массива
            b (int): Значение индекса для массива
            c (int): Значение индекса для массива
            d (int): Значение индекса для массива
        """
        x[b] ^= self.__rol(self.__sum(x[a], x[d]), 7)
        x[c] ^= self.__rol(self.__sum(x[b], x[a]), 9)
        x[d] ^= self.__rol(self.__sum(x[c], x[b]), 13)
        x[a] ^= self.__rol(self.__sum(x[d], x[c]), 18)

    def __generate_ks(self):
        """Генерирует ключевой поток
        
        Returns:
            bytes: 64-байтовый поток ключей
        """        
        x = self.__state[:]
        for i in range(10):
            self.__QR(x, 0, 4, 8, 12)
            self.__QR(x, 5, 9, 13, 1)
            self.__QR(x, 10, 14, 2, 6)
            self.__QR(x, 15, 3, 7, 11)

            self.__QR(x, 0, 1, 2, 3)
            self.__QR(x, 5, 6, 7, 4)
            self.__QR(x, 10, 11, 8, 9)
            self.__QR(x, 15, 12, 13, 14)
        out = []
        
        for i in range(len(self.__state)):
            out.append((self.__state[i] ^ x[i]) & self.__MAX_NUM)
        out = struct.pack('<16I',
                        out[0],  out[1],  out[2],  out[3],
                        out[4],  out[5],  out[6],  out[7],
                        out[8],  out[9],  out[10], out[11],
                        out[12], out[13], out[14], out[15])
        return out
    
    def Encrypt(self, data:str, key:str, nonce:str)->str:
        """Шифрование и расшифрование данных

        Args:
            data (str): Даннные для обработки
            key (str): Ключ, используемый для шифрования данных 32 байта
            nonce (str): Одноразовая номер, используемая для генерации keystate

        Returns:
            str: Результат обработки
        """        
        res = ''
        for i in range(0, len(data), self.__COUNTER_LENGTH):
            block = data[i : i + self.__COUNTER_LENGTH]
            self.__setup_keystate(key.encode("utf-8"), nonce.encode("utf-8"), i // self.__COUNTER_LENGTH)
            ks = self.__generate_ks()
            for x in range(len(block)):
                res += chr(ord(block[x]) ^ ks[x])
        return res