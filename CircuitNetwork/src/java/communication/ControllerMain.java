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

/**
 *
 * @author valeriysosnovskiy
 */
public class ControllerMain {
   public ControllerMain(String path) {
        emailTo = path;
    }
   String emailTo; 
  
   public String emailMessage(String emailTo) {
            //recipients email
            String to = "valeriysosnovskiy@gmail.com";
            String emailAddress = emailTo;
            //sender
            String from = emailAddress;
            //localhost
            String host = "localhost:8080/CircuitNetwork/ContactUs.html";
            //get the properties
            Properties properties = System.getProperties();
            
            //setup mail server
            properties.setProperty("mail.smtp.host", host);
            
            //get session object
            Session session = Session.getDefaultInstance(properties);
            
            try{
                 // Create a default MimeMessage object.
                 MimeMessage message = new MimeMessage(session);

                // Set From: header field of the header.
               message.setFrom(new InternetAddress(from));

               // Set To: header field of the header.
                message.addRecipient(Message.RecipientType.TO,
                                  new InternetAddress(to));

                // Set Subject: header field
                
                 message.setSubject("iGEm");
                 

                // Now set the actual message
                message.setText("The contact page is done ");

                // Send message
                Transport.send(message);
                System.out.println("Sent message successfully....");
      
            }catch (MessagingException mex) {
         mex.printStackTrace();
      }
            return emailAddress;
   }
            
            
        }
   
        
   

