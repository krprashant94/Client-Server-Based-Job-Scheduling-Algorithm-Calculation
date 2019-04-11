import java.io.*;
import java.net.*;
import java.util.List;
import java.util.ArrayList;
public class SJFServer
{
    public static void main(String[] args) throws Exception
    {
        ServerSocket sersock = new ServerSocket(3000);
        System.out.println("-----------------------------------");
        System.out.println("Server Ready");
        System.out.println("------------------------------------");
        Socket sock = sersock.accept( );                          
        BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
        OutputStream ostream = sock.getOutputStream(); 
        PrintWriter pwrite = new PrintWriter(ostream, true);
        InputStream istream = sock.getInputStream();
        BufferedReader receiveRead = new BufferedReader(new InputStreamReader(istream));

        String receiveMessage, sendMessage;
        Process processList[] = null;
        int i = 0;
        while(true)
        {
            if((receiveMessage = receiveRead.readLine()) != null)  
            {
                try{
                    String[] parameter = receiveMessage.split(":");
                    Process p = new Process(Integer.parseInt(parameter[0]), Integer.parseInt(parameter[1]), Integer.parseInt(parameter[2]));
                    i++;
                    processList = addElement(processList, p, i);
                    SJF sj = new SJF();
                    float times[] = sj.findavgTime(processList, processList.length); 

                    pwrite.println("Average waiting time = " + String.valueOf(times[0]) +"  Average turn around time = " + String.valueOf(times[1]));
                    pwrite.flush();
                }catch(Exception e){
                    pwrite.println("Unformatted String");             
                    pwrite.flush();
                    e.printStackTrace();
                }
            }
        }               
    }         

    static Process[] addElement(Process[] a, Process e, int len) {
        Process p[] = new Process[len];
        int i=0;
        if(a == null){
            p[0] = e;
            return p;
        }
        
        for (i=0; i<len-1; i++) {
            p[i] = a[i];
        }
        p[i] = e;
        return p;
    }           
}
