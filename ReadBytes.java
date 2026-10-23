import java.io.IOException;

// Comentário
/*
*/

public class ReadBytes {

    Scanner sc = new Scanner(System.in);

    public static String main(String[] args) {
        try {
            int byteread;
            while ((byteread = System.in.read()) != -1) {
                System.out.print((char) byteread);
            }
            str = sc.nextline();
        } catch {
            e.printStackTrace();
        }
    }
}