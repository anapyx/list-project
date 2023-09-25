# -*- coding: utf-8 -*-

import numpy as np
import customtkinter

from No import No
from LSE import LSE

class LDE():
    def __init__(self, head=None):
        self.head = head
        self.content = None
        if head == None:
            self.len = 0
        else:
            self.len = 1
        self.node_radius = 45
        self.node_spacing = 30
        self.vertical_position = 400
        self.tail = None
        
    # Verifica se a lista está vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False
        
    # Verifica se a lista está cheia    
    def full(self):
        if self.empty() == True:
            return False
        else:
            return True

    # Retorna o tamanho da lista
    def size(self):
        return self.len

            
    # Checa o elemento de determinada posição
    def element(self, pos):
        current = self.head
        aux = 1
        if self.empty():
            raise ValueError("A lista está vazia.")
        if pos < 1 or pos > self.len:
            raise ValueError("Posição inválida.")
        while aux < pos:
            current = current.getNext()
            aux += 1
        return current.getContent() 

    # Checa as posições de um determinado elemento
    def position(self, elem):
        count = 1
        
        if self.empty():
            raise ValueError("A lista está vazia.")
        
        aux = self.head
        
        while aux is not None:
            if isinstance(aux, No) and aux.getContent() == elem:
                return count
            aux = aux.getNext()
            count += 1
            
        raise ValueError("Nenhum elemento foi encontrado.")
    
    # Adiciona No em lista vazia
    def append(self, elem):
        newnode = No()
        newnode.setContent(elem)
        
        if self.empty():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.setNext(self.head)
            newnode.setPrevious(None)
            self.head.setPrevious(newnode)
            self.head = newnode
        
        self.len += 1
        
        return True
    
    # Adiciona No no meio da lista
    def appendAtMiddle(self, pos, elem):
        count = 1
        
        newnode = No(elem)
        
        aux = self.head
        
        while count < pos-1 and aux is not None:
            aux = aux.getNext()
            count += 1

        if aux is None:
            return False
        
        newnode.setPrevious(aux)
        newnode.setNext(aux.getNext())
        
        if aux.getNext() is not None:
            aux.getNext().setPrevious(newnode)
        
        aux.setNext(newnode)
        
        self.len += 1
        
        return True
    
    # Adiciona No no fim da lista
    def appendAtEnd(self, elem):
        newnode = No(elem)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.setNext(None)
            newnode.setPrevious(self.tail)

            if self.tail:
                self.tail.setNext(newnode)
            
            self.tail = newnode

        self.len += 1
        return True

    
    # Insercao de No em uma determinada posicao
    def appendList(self, elem, pos):
        if self.empty() == True:
            if pos == 1:
                self.head = elem
                self.len += 1
                return True
            else:
                return False
        
        if pos == 1:
            return self.append(elem)
        elif pos == self.len+1:
            return self.appendAtEnd(elem)
        else:
            return self.appendAtMiddle(pos, elem)
        
    # Remove No no inicio de uma lista unitaria
    def removeUnitaryList(self):
        value = self.head.getContent()
        self.head = None
        self.tail = None
        self.len -= 1
        
        return True
    
    # Remove No no inicio da lista
    def removeAtStart(self):
        aux = self.head
        
        value = aux.getContent()
        
        self.head = aux.getNext()
        aux.getNext().setPrevious(None)
        
        self.len -= 1
        
        aux = None
        
        return True
    
    # Remove No no meio da lista
    def removeAtMiddle(self, pos):
        aux = self.head
        count = 1
        
        while count <= pos-1 and aux is not None:
            aux = aux.getNext()
            count += 1
            
        if aux is None:
            raise ValueError("Posicao invalida.")
        
        value = aux.getContent()
        
        aux.getPrevious().setNext(aux.getNext())
        aux.getNext().setPrevious(aux.getPrevious())
        
        self.len -= 1
        
        aux = None
        
        return True
        
    # Remove No no fim da lista
    def removeAtEnd(self):
        if self.empty():
            raise ValueError("A lista está vazia.")

        if self.len == 1:
            return self.removeUnitaryList()
        
        aux = self.tail
        value = aux.getContent()
        aux.getPrevious().setNext(None)
        self.tail = aux.getPrevious()
        aux = None
        
        self.len -= 1
        return True
    
    # Controle da remocao de Nos em posicoes determinadas
    def remove(self, pos):
        if self.empty():
            raise ValueError("A lista está vazia")
        
        if pos == 1 and self.len == 1:
            return self.removeUnitaryList()
        elif pos == 1:
            return self.removeAtStart()
        elif pos == self.size():
            return self.removeAtEnd()
        else:
            return self.removeAtMiddle(pos)
        
    def draw_doubly_linked_list(self, canvas):
        canvas.delete("all")
        current = self.head
        x = 400
        y = 350

        while current:
            if isinstance(current, No):
                canvas.create_rectangle(x - self.node_radius, y - self.node_radius,
                                        x + self.node_radius, y + self.node_radius,
                                        fill= "#ffffff", outline = "#142c59")

                content = current.getContent()
                canvas.create_text(x, y, text=str(content), font=("Arial", 16))

                if current.getNext() and isinstance(current.getNext(), No):
                    canvas.create_line(x + self.node_radius, y,
                                    x + self.node_spacing - self.node_radius, y,
                                    arrow=customtkinter.LAST)

                if current.getPrevious() and isinstance(current.getPrevious(), No):
                    canvas.create_line(x - self.node_radius, y,
                                    x - self.node_spacing + self.node_radius, y,
                                    arrow=customtkinter.FIRST)

            current = current.getNext()  
            x += self.node_spacing 