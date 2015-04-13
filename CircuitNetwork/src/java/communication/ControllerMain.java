/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package communication;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author valeriysosnovskiy
 */
public class ControllerMain {

    public ControllerMain(String path) {
        rootPath = path;
    }
    String rootPath;

    /*
     *Sets the file path to execute 
     */
    public String runPython(String scriptName) {
        String output = executeCommand("python " + rootPath + "/" + scriptName); //append path to script name and then execute
        System.out.println("python " + rootPath + "/" + scriptName);
        return output;

    }

    public String executeQuery(String query) {
        System.out.println("python " + rootPath + "/sbider_network_builder.py " + rootPath + " " + query + "");
        String output = executeCommand("python " + rootPath + "/sbider_network_builder.py " + rootPath + " " + query); //append path to script name and then execute
        return output;

    }

    public String executeUpload(String upload) {
            String pigeonFilePath = executeCommand("python " + rootPath + "/sbider_upload_database.py " + rootPath + " " + upload);
        try {

            Thread.sleep(4000);
            File pigeonTextFile = new File(pigeonFilePath);
            
            PigeonToPNG.parseFile(pigeonTextFile); 
        } catch (InterruptedException ex) {
            Logger.getLogger(ControllerMain.class.getName()).log(Level.SEVERE, null, ex);
        }
            return pigeonFilePath;

    }

    //to execute the files 
    public String executeCommand(String command) {
        System.out.println("command: " + command);
        StringBuilder output = new StringBuilder();

        Process p;
        try {

            //System.out.println("Before running python script.");
            p = Runtime.getRuntime().exec(command);

            //System.out.println("After running python script.");
            p.waitFor();
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));

            String line = "";
            while ((line = reader.readLine()) != null) {
                output.append(line + "\n");
                //System.out.println("In the loop");
                System.out.println(line);
            }

            reader = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            line = "";
            while ((line = reader.readLine()) != null) {
                //System.out.println("In the loop");
                System.out.println(line);
            }

        } catch (Exception e) {

            e.printStackTrace();
            return "no result";
        }
        return output.toString();

    }

}
