package communication;
import java.util.Properties;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.BodyPart;
import javax.mail.Multipart;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMultipart;

public class GoogleMail {
    private final String userName;
    private final String userEmail;
    private final String userSubject;
    private final String userMessage;
    
    
    public GoogleMail(String userName, String userEmail, String userSubject, String userMessage) {
        
        this.userName = userName;
        this.userEmail = userEmail;
        this.userSubject = userSubject;
        this.userMessage = userMessage;
    }
    
    public void writeMessage() {
                
     // Recipient's email ID needs to be mentioned.
      String to = "sbiderapp@gmail.com";
      
      sendIt(to);
    }
    
    public void automationEmail(String user){
      String to = user; 
      
      sendIt(to);
    }
    
    public String sendIt(String to){
      // Sender's email ID needs to be mentioned
      String from = "sbiderapp@gmail.com";
      final String username = "sbiderapp@gmail.com";
      final String password = "ucsd2015";

      // Assuming you are sending email through relay.jangosmtp.net
      String host = "smtp.gmail.com";

      Properties props = new Properties();
      props.put("mail.smtp.auth", "true");
      props.put("mail.smtp.starttls.enable", "true");
      props.put("mail.smtp.host", host);
      props.put("mail.smtp.port", "587");

      // Get the Session object.
      Session session = Session.getInstance(props,
      new javax.mail.Authenticator() {
         protected PasswordAuthentication getPasswordAuthentication() {
            return new PasswordAuthentication(username, password);
         }
      });

      try {
         // Create a default MimeMessage object.
         Message message = new MimeMessage(session);

         // Set From: header field of the header.
         message.setFrom(new InternetAddress(from));

         // Set To: header field of the header.
         message.setRecipients(Message.RecipientType.TO,
         InternetAddress.parse(to));

         // Set Subject: header field
         message.setSubject(userSubject);

         // Now set the actual message
         message.setText("User name: " + userName + "\n" + "User email: " + userEmail+ "\n\n"+ "Message: \n" + userMessage);

         // Create the message part
         BodyPart messageBodyPart = new MimeBodyPart();
         
         // Create a multipar message
         Multipart multipart = new MimeMultipart();
         
         // Set text message part
         multipart.addBodyPart(messageBodyPart);

         // Part two is attachment
         messageBodyPart = new MimeBodyPart();
         String filename = "/home/manisha/file.txt";
         DataSource source = new FileDataSource(filename);
         messageBodyPart.setDataHandler(new DataHandler(source));
         messageBodyPart.setFileName(filename);
         multipart.addBodyPart(messageBodyPart);

         // Send the complete message parts
         message.setContent(multipart); 
         
         // Send message
         Transport.send(message);

         System.out.println("Sent message successfully....");

      } catch (MessagingException e) {
            throw new RuntimeException(e);
      }
      return ("thank you: "+ userName); 
	}

}