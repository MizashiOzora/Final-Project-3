-- Drop existing table if it exists
DROP TABLE IF EXISTS reservation;

-- Create the 'reservation' table
CREATE TABLE reservation (
    id SERIAL PRIMARY KEY,
    maskapai TEXT NOT NULL,
    tujuan TEXT NOT NULL,
    penumpang TEXT NOT NULL,
    nomor_pesawat TEXT NOT NULL,
    alamat TEXT NOT NULL,
    nomor_handphone TEXT NOT NULL,
    tanggal_berangkat DATE NOT NULL
);

-- Insert sample data
INSERT INTO reservation (maskapai, tujuan, penumpang, nomor_pesawat, alamat, nomor_handphone, tanggal_berangkat)
VALUES
    ('Garuda Indonesia', 'Surabaya', 'Ahmad Maulana', 'GA-123', 'address1', '62838', '2023-10-01'),
    ('Air Asia', 'Jakarta', 'Renata Zahab', 'AA-456', 'address2', '62838', '2022-10-02'),
    ('Citilink', 'Bali', 'Nunuk Reni', 'CT-789', 'address3', '62838', '2022-10-03'),
    ('Emirates', 'Lombok', 'Bro Ulil', 'EK-1011', 'address4', '62838', '2022-10-04'),
    ('Singapore Airlines', 'Bandung', 'Wah Bowi', 'SQ-1234', 'address5', '62838', '2022-10-05'),
    ('Garuda Indonesia', 'Surabaya', 'Iis Mika', 'GA-5678', 'address6', '62838', '2022-10-06'),
    ('Air Asia', 'Jakarta', 'Zizah Lana', 'AA-9012', 'address7', '62838', '2022-10-07'),
    ('Citilink', 'Bali', 'Alif Iman', 'CT-1357', 'address8', '62838', '2022-10-08'),
    ('Emirates', 'Lombok', 'Zaka Zaki', 'EK-1689', 'address9', '62838', '2022-10-09'),
    ('Singapore Airlines', 'Bandung', 'Faus Rahmi', 'SQ-2022', 'address10', '62838', '2022-10-11');
