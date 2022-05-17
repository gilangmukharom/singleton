class SingletonMeta(type):
    """
    Singleton class dapat diimplementasikan dengan berbagai metode menggunakan Python. Beberapa
    metode yang mungkin termasuk: kelas dasar, decorator, metaclass. disini akan menggunakan
    metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Kemungkinan perubahan nilai argumen `__init__` tidak mempengaruhi
        hasil instance yang dikembalikan.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Akhirnya, singleton harus mendefinisikan beberapa logikanya, yang dapat
        dieksekusi pada instance.
        """

        # ...


if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton berhasil, variabel sama dengan instance.")
    else:
        print("Singleton gagal dijalankan, variabel tidak sama dengan instance.")