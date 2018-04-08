




import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;

public class main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException {
        // TODO code application logic here
        String lines[] = null;
        String s="D:\\Hager Docs\\CMP\\Fourth Year\\Graduation Project\\TextRecognation\\Kinds\\10000_cigarettes.pdf";
        readfile r = new readfile();
        if(s.toLowerCase().endsWith(".txt")){
            lines=r.readtxt(s);
            System.out.println("Document text") ;
        }
        else if (s.toLowerCase().endsWith(".pdf")){
            lines=r.readpdf(s);
            System.out.println("PDF File") ;
        }
        else
            System.out.println("error please insrt pdf /txt file ") ;
        System.out.println(lines.length) ;
        PrintWriter writer = new PrintWriter(lines[0]+".txt", "UTF-8");
        for (String line : lines) {
            writer.println(line);
        }
        writer.close();

    }
    
}
