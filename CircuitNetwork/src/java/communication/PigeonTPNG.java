/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import javax.swing.JFileChooser;

/**
 *
 * @author Jenhan Tao <jenhantao@gmail.com>
 */
public class PigeonTPNG {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        JFileChooser fc = new JFileChooser();
        fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        fc.showOpenDialog(null);
        File selectedDirectory = fc.getSelectedFile();
        parseDirectory(selectedDirectory);
    }

    private static void parseDirectory(File directory) {
        File[] files = directory.listFiles();
        for (File file : files) {
            if (file.isFile()) {
                if (file.getAbsolutePath().contains("txt")) {
                    parseFile(file);

                }
            }
        }
    }

    private static void parseFile(File file) {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(file.getAbsolutePath()));
            String line = reader.readLine();
            String toSubmit = "";
            while (line != null) {
                toSubmit = toSubmit + line + "\n";
                line = reader.readLine();
            }
            System.out.println(toSubmit);
            WeyekinPoster.setPigeonText(toSubmit);
            WeyekinPoster.setShouldILaunchBrowserPage(true);
            WeyekinPoster.postMyBird();
            System.out.println(WeyekinPoster.getmPigeonURI());

            //download image
            URL url = WeyekinPoster.getmPigeonURI().toURL();

            BufferedInputStream in = null;
            FileOutputStream fout = null;
            try {
                in = new BufferedInputStream(url.openStream());
                fout = new FileOutputStream(file.getAbsolutePath().replace("txt", "png"));

                byte data[] = new byte[1024];
                int count;
                while ((count = in.read(data, 0, 1024)) != -1) {
                    fout.write(data, 0, count);
                }
            } finally {
                if (in != null) {
                    in.close();
                }
                if (fout != null) {
                    fout.close();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
