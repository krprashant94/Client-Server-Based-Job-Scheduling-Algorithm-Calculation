import java.io.*;
import java.net.*;
import java.util.List;
import java.util.ArrayList;
public class GFGServer
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
        int processes[] = null;
        int burst_time[] = null;
        int i = 0;
        while(true)
        {
            if((receiveMessage = receiveRead.readLine()) != null)  
            {
                try{
                    i++;
                    String[] parameter = receiveMessage.split(":");
                    processes = addElement(processes, Integer.parseInt(parameter[0]), i);
                    burst_time = addElement(burst_time, Integer.parseInt(parameter[1]), i);
                    GFG r = new GFG();
                    float times[] = r.findavgTime(processes, i, burst_time);

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

    static int[] addElement(int[] a, int e, int len) {
        System.out.println(len);
        int p[] = new int[len];
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
