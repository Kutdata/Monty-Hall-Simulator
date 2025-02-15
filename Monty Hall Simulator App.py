# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:49:28 2025

@author: MUSTAFA
"""

import random
import tkinter as tk

class MontyHallSimulator:
    def __init__(self, num_trials):
        self.num_trials = num_trials
        self.same_choice_wins = 0
        self.switched_choice_wins = 0
    
    def run_simulation(self):
        for _ in range(self.num_trials):
            doors = ['gold', 'goat', 'goat']
            random.shuffle(doors)
            
            first_choice = random.randint(0, 2)
            #Monty'in alacağı kapı
            possible_doors_to_open = [i for i in range(3) if i != first_choice and doors[i] == 'goat']
            monty_opens = random.choice(possible_doors_to_open)
            #Oyuncunun değiştirme seçeneği
            remaining_door = [i for i in range(3) if i != first_choice and i != monty_opens][0]
            #İlk seçimde kazanma ihtimali
            if doors[first_choice] == 'gold':
                self.same_choice_wins += 1
            #İkinci seçimde kazanma ihtimali
            if doors[remaining_door] == 'gold':
                self.switched_choice_wins += 1
    def get_results(self):
        return self.same_choice_wins, self.switched_choice_wins

class MontyHallApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x150')
        self.root.title('Monty Hall Simulatörü')
        self.root.resizable(0, 0)
        #Değişkenler
        self.same_choice = tk.StringVar(value = '0')
        self.switched_choice = tk.StringVar(value = '0')
        #Arayüz Elemanları
        tk.Label(root, text = 'Deneme Sayısı').place(x=50, y=10)
        self.entry_samples = tk.Entry(root)
        self.entry_samples.place(x=150, y=10)
        
        tk.Label(root, text = 'Aynı Tercihle Kazanç').place(x=50, y=50)
        tk.Label(root, text = 'Değiştirerek Kazanç').place(x=50, y=80)
        tk.Label(root, textvariable=self.same_choice, font=(15)).place(x=200, y=50)
        tk.Label(root, textvariable=self.switched_choice, font=(15)).place(x=200, y=80)
        #Simulasyonu Çalıştır
        self.entry_samples.bind('<Return>', self.run_simulation)
    
    def run_simulation(self, event):
        try:
            num_samples = int(self.entry_samples.get())
            #MontyHall simulatörünü çalıştır
            simulator = MontyHallSimulator(num_samples)
            simulator.run_simulation()
            same, switched = simulator.get_results()
            #Sonuçları arayüzde göster
            self.same_choice.set(str(same))
            self.switched_choice.set(str(switched))
        except ValueError:
            self.same_choice.set('Hata!')
            self.switched_choice.set('Lütfen sayı giriniz.'),
if __name__ == '__main__':
    root = tk.Tk()
    app = MontyHallApp(root)
    root.mainloop()
            
            
        
        
        
