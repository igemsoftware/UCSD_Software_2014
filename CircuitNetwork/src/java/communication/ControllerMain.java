/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package communication;

import java.io.BufferedReader;
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
import com.sun.mail.smtp.SMTPTransport;
import java.security.Security;
import java.util.Date;
import java.util.Properties;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;


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
        System.out.println("python " + rootPath + "/sbider_network_builder.py "+rootPath +" " + query+"");
        String output = executeCommand("python " + rootPath + "/sbider_network_builder.py "+rootPath +" " + query); //append path to script name and then execute
        return output;

    }

    

    
    //to execute the files 
    public String executeCommand(String command) {
        System.out.println("command: " + command);
        StringBuilder output = new StringBuilder();

        Process p;
        try {
            p = Runtime.getRuntime().exec(command);
            p.waitFor();
//            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getErrorStream()));

            String line = "";
            while ((line = reader.readLine()) != null) {
                output.append(line + "\n");
                System.out.println(line);
            }

        } catch (Exception e) {
            e.printStackTrace();
            return "no result";
        }
        return output.toString();

    }
    
}
