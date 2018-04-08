/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Hager - Lab
 */
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;
import org.apache.pdfbox.text.PDFTextStripperByArea;
public class readfile {
    String lines[] ;
    public String[] readpdf( String s )
    {
        try (PDDocument document = PDDocument.load(new File(s))) {

            document.getClass();
            if (!document.isEncrypted()) {
			
                PDFTextStripperByArea stripper = new PDFTextStripperByArea();
                stripper.setSortByPosition(true);

                PDFTextStripper tStripper = new PDFTextStripper();

                String pdfFileInText = tStripper.getText(document);
                //System.out.println("Text:" + st);
                List<String> temps = new ArrayList<String>();
				// split by whitespace
                String lines2[]  = pdfFileInText.split("\\r?\\n");
                for (String line : lines2) {
                    line=line.trim();
                    if(line.length() == 0){
//                        System.out.println("11");
                        continue;
                     }
                    temps.add(line);
//                    System.out.println(line);
                
                }
                lines = temps.toArray(new String[0]);

            }

        } catch (IOException ex) {
            Logger.getLogger(main.class.getName()).log(Level.SEVERE, null, ex);
        }
        return lines;
    }
    
    public String[] readtxt( String s )
    {
        BufferedReader br = null;
	FileReader fr = null;

        try {
            fr = new FileReader(s);
            br = new BufferedReader(fr);
            List<String> temps = new ArrayList<String>();
            String sCurrentLine;

            while ((sCurrentLine = br.readLine()) != null) {
//                    System.out.println(sCurrentLine);
                    sCurrentLine=sCurrentLine.trim();
                    if (sCurrentLine.length()==0)
                        continue;
                    temps.add(sCurrentLine);
            }
            
        lines = temps.toArray(new String[0]);

        } catch (IOException e) {

            e.printStackTrace();

        } finally {

            try {

                if (br != null)
                        br.close();

                if (fr != null)
                        fr.close();

            } catch (IOException ex) {

                ex.printStackTrace();

            }
        }
        return lines;
    }
}
//"D:\\Hager Docs\\CMP\\Fourth Year\\Graduation Project\\TextRecognation\\Kinds\\10000_cigarettes.txt"