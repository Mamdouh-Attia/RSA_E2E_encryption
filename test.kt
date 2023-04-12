//function to send the data via wifi where IP: 192.168.1.4 to esp32
fun sendWifiData(data: String) {
    val socket = Socket("192.168.1.4", 8080)
    val out = PrintWriter(socket.getOutputStream(), true)
    out.println(data)
    out.close()
    socket.close()
}




