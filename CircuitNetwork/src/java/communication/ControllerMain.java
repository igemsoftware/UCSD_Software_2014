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
import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
import javax.activation.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/**
 *
 * @author valeriysosnovskiy
 */
public class ControllerMain {
    public ControllerMain(String path) {
        rootPath = path;
    }
    String rootPath;
    
        public String runPython(String scriptName) {
            String output = executeCommand("python "+rootPath+"/"+scriptName); //append path to script name and then execute
            System.out.println(output);
            return output;
            
        }
        
        
        //trying to set up the hashMap for the login 
        public String storeInfo(String userName, String userPassword){
            System.out.println("storeInfo");
            Map info = new HashMap();
            Iterator iterateThis = info.entrySet().iterator();
           
            while(iterateThis.hasNext()){
                
                Map.Entry entry = (Map.Entry) iterateThis.next();
                System.out.println(entry.getKey() + " " + entry.getValue());
                  if(info.containsKey(userName) ){
                      System.out.println("user already exists");
                  }
                  else{
                    System.out.println("user already exists");
                    info.put(userName, userPassword);
                      System.out.println("new user welcome");
                }
                  System.out.println("info");
                }
            
        
            
           
           return (userName);
        }
        
        //to execute the files 
        public String executeCommand(String command) {
        System.out.println(command);
        StringBuilder output = new StringBuilder();

        Process p;
        try {
            p = Runtime.getRuntime().exec(command);
            p.waitFor();
            BufferedReader reader
                    = new BufferedReader(new InputStreamReader(p.getInputStream()));

            String line = "";
            while ((line = reader.readLine()) != null) {
                output.append(line + "\n");
            }

        } catch (Exception e) {
            e.printStackTrace();
            return "no result";
        }

        return output.toString();

    }
}
