import qrcode
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import io


def generate_qr_code():
    """
    Generate a QR code from the user input and display it in a window
    """
    # Create window for input and display
    window = tk.Tk()
    window.title("QR Kod Oluşturucu")
    window.configure(bg='#e6e6e6')

    # Create main frame with custom style
    style = ttk.Style()
    style.configure('Custom.TFrame', background='#e6e6e6')
    frame = ttk.Frame(window, padding="25", style='Custom.TFrame')
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Configure styles
    style.configure('Custom.TLabel', background='#e6e6e6', font=('Arial', 11))
    style.configure('Custom.TButton', font=('Arial', 11, 'bold'), padding=6)
    style.configure('Title.TLabel', background='#e6e6e6', font=('Arial', 16, 'bold'))

    # Title
    title_label = ttk.Label(frame, text="QR Kod Oluşturucu", style='Title.TLabel')
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 25))

    # Create input field with modern styling
    url_label = ttk.Label(frame, text="URL Girin:", style='Custom.TLabel')
    url_label.grid(row=1, column=0, pady=8)
    url_entry = ttk.Entry(frame, width=55, font=('Arial', 11))
    url_entry.grid(row=1, column=1, pady=8, padx=8)

    def generate():
        data = url_entry.get()
        if not data:
            messagebox.showwarning("Uyarı", "Lütfen önce bir URL girin!")
            return

        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,  # Increased box size for larger QR code
            border=4,
        )

        # Add data to QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code
        qr_photo = ImageTk.PhotoImage(qr_image)
        if hasattr(frame, 'qr_label'):
            frame.qr_label.destroy()
        frame.qr_label = ttk.Label(frame, image=qr_photo, style='Custom.TLabel')
        frame.qr_label.image = qr_photo  # Keep a reference!
        frame.qr_label.grid(row=3, column=0, columnspan=2, pady=25)

        # Resize window to fit larger QR code
        window.update_idletasks()
        window.geometry(f"{qr_image.size[0] + 100}x{qr_image.size[1] + 200}")

        # Re-center the window
        x = (window.winfo_screenwidth() // 2) - (window.winfo_width() // 2)
        y = (window.winfo_screenheight() // 2) - (window.winfo_height() // 2)
        window.geometry(f"+{x}+{y}")

    # Button frame for better organization
    button_frame = ttk.Frame(frame, style='Custom.TFrame')
    button_frame.grid(row=2, column=0, columnspan=2, pady=20)

    # Generate button with improved styling
    generate_button = ttk.Button(
        button_frame,
        text="QR Kod Oluştur",
        command=generate,
        style='Custom.TButton'
    )
    generate_button.grid(row=0, column=0, padx=8)

    # Add a close button
    close_button = ttk.Button(
        button_frame,
        text="Kapat",
        command=window.destroy,
        style='Custom.TButton'
    )
    close_button.grid(row=0, column=1, padx=8)

    # Center the window on screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.mainloop()


if __name__ == "__main__":
    generate_qr_code()
