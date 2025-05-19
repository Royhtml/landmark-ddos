import socket as sck
import struct

# oenyerangan ddos yang untuk mengunjungi dan beraktifitas secara pintar

class Landmark:
    # tentukan pengiriman host server inet port ddos
    def __init__(self):
        self.host = '103.156.118.244' # kalian bisa ganti dengan server yang ingin di serang sekarang ini
        self.port = 204 # kalian bisa masukan port anda yang ingin di tuju ke port server yang di serang sekaranag ini
        self.sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        
    # ini adalah fungsi mengirim ke server
    def send_data(self, data):
        self.sock.send(data)

# menerima pengiriman sampah pada server
    def receive_data(self):
        data = self.sock.recv(1024)
        return data

    def close_connection(self):
        self.sock.close()
        
    # fungsinya akan masuk ke server dan pengiriman name jikalu sdah benar semuah di masukan pada host server
    def get_landmark(self):
        data = self.receive_data()
        landmark = struct.unpack('!f', data)
        return landmark
    def set_landmark(self, landmark):
        data = struct.pack('!f', landmark)
        self.send_data(data)
    # data akan masuk dan menampilkan penyerangan landmark pintar
    def get_landmark_list(self):
        data = self.receive_data()
        landmark_list = struct.unpack('!f' * (len(data) // 4), data)
        return landmark_list
    def set_landmark_list(self, landmark_list):
        data = struct.pack('!f' * (len(landmark_list)), *landmark_list)
        self.send_data(data)
        
if __name__ == "__main__": # jikalau benar akan masuk penyerangan ddos landmark pada server [pintar]
    landmark = Landmark()
    landmark.set_landmark(0.5)
    print("landmark : ", landmark.get_landmark())
    landmark.set_landmark_list([0.1, 0.2, 0.3])
    print("landmark list : ", landmark.get_landmark_list())
    landmark.close_connection()
    send_data = landmark.set_landmark(0.5)
    receive_data = landmark.receive_data()
    landmark.close_connection()
    print("send data : ", send_data)
    print("receive data : ", receive_data)
    # tambahakan module ddos untuk menjalankan ddos pintar
