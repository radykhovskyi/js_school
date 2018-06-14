# -*- coding: utf-8 -*- 


class Emitter:
    __handlers = {}

    def __init__(self):
        """Создает экземпляр класса Emitter."""
        pass

    def on(self, event, handler):
        """ связывает обработчик handler с событием event

        Parameters
        ---------
        event : str
            событие
        handler : func
            обработчик
        """
        if event not in self.__handlers: self.__handlers[event] = []
        self.__handlers[event].append(handler)

    def emit(self, event, data):
        """ Генерирует событие event -- вызывает все связанные с ним
            обработчики, в которые передает аргумент data

        Parameters
        ----------
        event : str
            событие
        data
            данные, которые необходимо передать обработчикам
        """
        if event in self.__handlers:
            for handler in self.__handlers[event]:
                handler(data)
