package communication;
import java.util.Properties;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class GoogleMail {
    private String userName;
    private String userEmail;
    private String userSubject;
    private String userMessage;
    
    
    public GoogleMail(String userName, String userEmail, String userSubject, String userMessage) {
        
        this.userName = userName;
        this.userEmail = userEmail;
        this.userSubject = userSubject;
        this.userMessage = userMessage;
    }
    
    public String writeMessage() {
                
     // Recipient's email ID needs to be mentioned.
      String to = "sbiderapp@gmail.com";

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
         message.setText("User name: " + userName + "\n" + "User email: " + userEmail+ "\n" + userMessage);

         // Send message
         Transport.send(message);

         System.out.println("Sent message successfully....");

      } catch (MessagingException e) {
            throw new RuntimeException(e);
      }
      return ("thank you: "+ userName); 
	}

}