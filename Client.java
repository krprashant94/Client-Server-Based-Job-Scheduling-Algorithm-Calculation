import java.io.*;
import java.net.*;
public class Client
{
    public static void main(String[] args) throws Exception
    {
        Socket sock = new Socket("127.0.0.1", 3000);
        BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
        OutputStream ostream = sock.getOutputStream(); 
        PrintWriter pwrite = new PrintWriter(ostream, true);

        InputStream istream = sock.getInputStream();
        BufferedReader receiveRead = new BufferedReader(new InputStreamReader(istream));

        System.out.println("------------------------------------");
        System.out.println("Send Data");
        System.out.println("------------------------------------");
        System.out.println("Round Robin :- PROCESS_ID:BUST_TIME:TIME_QUANTAM");
        System.out.println("SJF         :- PROCESS_ID:BUST_TIME:ARRIVAL_TIME");
        System.out.println("------------------------------------");

        String receiveMessage, sendMessage;               
        while(true)
        {
            sendMessage = keyRead.readLine();
            pwrite.println(sendMessage);
            pwrite.flush();
            if((receiveMessage = receiveRead.readLine()) != null)
            {
                System.out.println(receiveMessage);
            }         
        }               
    }               
}                        