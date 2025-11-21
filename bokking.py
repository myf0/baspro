import tkinter as tk
from tkinter import messagebox

class HotelSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sistem Manajemen Hotel")
        self.window.geometry("500x400")
        
        # Data sederhana (belum pakai database)
        self.users = {
            "admin": "admin123",
            "user1": "user123"
        }
        
        self.rooms = [
            {"id": 1, "type": "Standard", "price": 300000, "available": True},
            {"id": 2, "type": "Deluxe", "price": 500000, "available": True},
            {"id": 3, "type": "Suite", "price": 800000, "available": True}
        ]
        
        self.bookings = []
        
        self.show_login()
    
    def show_login(self):
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Login Frame
        self.login_frame = tk.Frame(self.window)
        self.login_frame.pack(pady=50)
        
        tk.Label(self.login_frame, text="LOGIN SISTEM HOTEL", 
                font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
        
        tk.Label(self.login_frame, text="Username:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.login_frame, text="Password:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        
        login_btn = tk.Button(self.login_frame, text="Login", command=self.check_login,
                             bg="blue", fg="white", font=("Arial", 12))
        login_btn.grid(row=3, column=0, columnspan=2, pady=20)
    
    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.users and self.users[username] == password:
            if username == "admin":
                self.show_admin_menu()
            else:
                self.show_customer_menu()
        else:
            messagebox.showerror("Error", "Username atau password salah!")
    def show_admin_menu(self):
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Header
        header = tk.Label(self.window, text="MENU ADMIN", 
                         font=("Arial", 16, "bold"), fg="blue")
        header.pack(pady=20)
        
        # Buttons
        btn_style = {"bg": "lightblue", "font": ("Arial", 12), "width": 20, "height": 2}
        
        tk.Button(self.window, text="Lihat Semua Kamar", 
                 command=self.show_all_rooms, **btn_style).pack(pady=10)
        
        tk.Button(self.window, text="Lihat Transaksi", 
                 command=self.show_transactions, **btn_style).pack(pady=10)
        
        tk.Button(self.window, text="Logout", 
                 command=self.show_login, bg="red", fg="white", 
                 font=("Arial", 10)).pack(pady=20)
    
    def show_all_rooms(self):
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        tk.Label(self.window, text="DAFTAR KAMAR", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        # Room list
        for i, room in enumerate(self.rooms):
            status = "Tersedia" if room["available"] else "Terbooking"
            color = "green" if room["available"] else "red"
            
            room_text = f"Kamar {room['id']} - {room['type']} - Rp {room['price']} - "
            room_label = tk.Label(self.window, text=room_text, font=("Arial", 10))
            room_label.pack()
            
            status_label = tk.Label(self.window, text=status, fg=color, font=("Arial", 10, "bold"))
            status_label.pack()
        
        tk.Button(self.window, text="Kembali", command=self.show_admin_menu,
                 bg="gray", fg="white").pack(pady=20)
    
    def show_transactions(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        
        tk.Label(self.window, text="RIWAYAT TRANSAKSI", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        if not self.bookings:
            tk.Label(self.window, text="Belum ada transaksi", 
                    font=("Arial", 12)).pack(pady=20)
        else:
            for booking in self.bookings:
                booking_text = f"Kamar {booking['room_id']} - {booking['customer']} - {booking['date']}"
                tk.Label(self.window, text=booking_text, font=("Arial", 10)).pack()
        
        tk.Button(self.window, text="Kembali", command=self.show_admin_menu,
                 bg="gray", fg="white").pack(pady=20)
    def show_customer_menu(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        
        header = tk.Label(self.window, text="PILIH KAMAR", 
                         font=("Arial", 16, "bold"), fg="darkgreen")
        header.pack(pady=20)
        
        # Available rooms
        available_rooms = [room for room in self.rooms if room["available"]]
        
        if not available_rooms:
            tk.Label(self.window, text="Maaf, tidak ada kamar tersedia", 
                    font=("Arial", 12)).pack(pady=20)
        else:
            for room in available_rooms:
                room_frame = tk.Frame(self.window, relief="solid", bd=1)
                room_frame.pack(pady=5, padx=20, fill="x")
                
                room_info = f"Kamar {room['id']} - {room['type']} - Rp {room['price']}/malam"
                tk.Label(room_frame, text=room_info, font=("Arial", 11)).pack(pady=5)
                
                book_btn = tk.Button(room_frame, text="Pesan Sekarang", 
                                   command=lambda r=room: self.book_room(r),
                                   bg="green", fg="white", font=("Arial", 10))
                book_btn.pack(pady=5)
        
        tk.Button(self.window, text="Logout", command=self.show_login,
                 bg="red", fg="white", font=("Arial", 10)).pack(pady=20)
    
    def book_room(self, room):
        # Simple booking process
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        booking = {
            "room_id": room["id"],
            "customer": self.username_entry.get(),  # dari login
            "date": current_time
        }
        
        self.bookings.append(booking)
        room["available"] = False
        
        messagebox.showinfo("Sukses", f"Kamar {room['id']} berhasil dipesan!")
        self.show_customer_menu()
# Jalankan program
if __name__ == "__main__":
    app = HotelSystem()
    app.window.mainloop()