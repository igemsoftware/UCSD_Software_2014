package communication;

//import java.io.BufferedInputStream;
//import java.io.BufferedReader;
//import java.io.File;
import java.io.FileOutputStream;
//import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
//import java.util.*;
import javax.servlet.ServletException;
//import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
//import java.lang.Object;
import java.net.URL;
//import java.nio.ByteBuffer;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;
//import java.nio.channels.WritableByteChannel;
//import org.json.simple.JSONObject; 
/**
 *
 * @author Admin
 */
public class AuthenticationServlet extends HttpServlet {

    /**
     * Processes requests for HTTP <code>POST</code> methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processPostRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
            //get json data parameters sent by client
            //String user = request.getParameter("user");
            //String password = request.getParameter("password");
            
            
            String text = "digraph{\n{rank=same; \nPIGEON_START\n\"a\"\no A 9\np pBad 4\no B 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"b\"\no B 9\nr a 5\no C 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"c\"\no C 9\nc tetR 8\no D 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"d\"\no D 9\nt a 6\no E 9\n# Arcs\nPIGEON_END\n}\n\n\"bc\" [shape=point, width=0.14159];\n\"bcd\" [shape=point, width=0.14159];\n\"bba\" [shape=point, width=0.14159];\nPIGEON_START\n\"abcd\"\no A 9\np pBad 4\no B 9\nr a 5\no C 9\nc tetR 8\no D 9\nt a 6\no E 9\n# Arcs\nPIGEON_END\n\n\"b\"->\"bc\" [label=\"3\", arrowhead=\"none\"];\n\"c\"->\"bc\" [label=\"3\", arrowhead=\"none\"];\n\"bc\"->\"bcd\" [label=\"3\", arrowhead=\"none\"];\n\"d\"->\"bcd\" [label=\"3\", arrowhead=\"none\"];\n\"a\"->\"bba\" [label=\"3\", arrowhead=\"none\"];\n\"bcd\"->\"bba\" [label=\"3\", arrowhead=\"none\"];\n\"bba\"->\"abcd\";\n\n\"bc\"->\"bc\" [taillabel=\"3 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\"bcd\"->\"bcd\" [taillabel=\"6 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\"abcd\"->\"abcd\" [taillabel=\"9 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\n}\n";
            String pigeonText = "digraph{\n{rank=same; \nPIGEON_START\n\"a\"\no A 9\np pBad 4\no B 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"b\"\no B 9\nr a 5\no C 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"c\"\no C 9\nc tetR 8\no D 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"d\"\no D 9\nt a 6\no E 9\n# Arcs\nPIGEON_END\n}\n\n\"bc\" [shape=point, width=0.14159];\n\"bcd\" [shape=point, width=0.14159];\n\"bba\" [shape=point, width=0.14159];\nPIGEON_START\n\"abcd\"\no A 9\np pBad 4\no B 9\nr a 5\no C 9\nc tetR 8\no D 9\nt a 6\no E 9\n# Arcs\nPIGEON_END\n\n\"b\"->\"bc\" [label=\"3\", arrowhead=\"none\"];\n\"c\"->\"bc\" [label=\"3\", arrowhead=\"none\"];\n\"bc\"->\"bcd\" [label=\"3\", arrowhead=\"none\"];\n\"d\"->\"bcd\" [label=\"3\", arrowhead=\"none\"];\n\"a\"->\"bba\" [label=\"3\", arrowhead=\"none\"];\n\"bcd\"->\"bba\" [label=\"3\", arrowhead=\"none\"];\n\"bba\"->\"abcd\";\n\n\"bc\"->\"bc\" [taillabel=\"3 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\"bcd\"->\"bcd\" [taillabel=\"6 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\"abcd\"->\"abcd\" [taillabel=\"9 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\n}";
            
            // pigeonText is a string in pigeon format;
            System.out.println(pigeonText);
            WeyekinPoster.setDotText(pigeonText);
            //out.println(pigeonText);
            // submit the post request--not working for some reason!
            WeyekinPoster.postMyVision();
            String imageURL = WeyekinPoster.getmGraphVizURI().toString();
            //out.println("waiting5");
            // successful post returns a url to an image
            //out.println(imageURL);
            response.sendRedirect(imageURL);
            WeyekinPoster.postMyBird();
            //System.out.println(WeyekinPoster.getmPigeonURI());     
            URL url = WeyekinPoster.getmPigeonURI().toURL();
       
            ReadableByteChannel rbc = Channels.newChannel(url.openStream());
            FileOutputStream fos = new FileOutputStream("C:\\Users\\Admin\\Documents\\GitHub\\UCSD_IGEM\\CircuitNetwork\\build\\myfile.jpeg");
            fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);
            
            
            //create a new cookie named authenticate with value authenticated
            /*Cookie authenticateCookie = new Cookie("authenticate", "authenticated");
               set the age of the cookie
            authenticateCookie.setMaxAge(60 * 60); //cookie lasts for an hour
                add cookie to responsej
            response.addCookie(authenticateCookie);*/
            
    }

    


/**
 * Processes requests for HTTP <code>POST</code> methods.
 *
 * @param request servlet request
 * @param response servlet response
 * @throws ServletException if a servlet-specific error occurs
 * @throws IOException if an I/O error occurs
 */
protected void processGetRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        //response.sendRedirect("index.html");
        //JSONObject obj = new JSONObject();
        String user = request.getParameter("key");
        PrintWriter out = response.getWriter();
        try {
            out.println("data from the server22323");
        } finally {
            out.close();
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP
     * <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
        protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processGetRequest(request, response);
    }

    /**
     * Handles the HTTP
     * <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
        protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processPostRequest(request, response);
        /** Create cookies for first and last names.   
      File file = new File ("info.txt");   
      PrintWriter out1 = new PrintWriter(file);
      try 
      {
        out1.println("kp"+"puri"+"\n"+"jenhan"+"tao");
        
            
      Hashtable login = new Hashtable();
      login.put("kp", "puri");
      login.put("valeriy", "sosnovskiy");
      login.put("lauren", "crudup");
      
      String firstN = request.getParameter("first_name");
      String lastN = request.getParameter("last_name");
      
      Cookie firstName = new Cookie("first_name",
                      request.getParameter("first_name"));
      Cookie lastName = new Cookie("last_name",
                      request.getParameter("last_name"));

      // Set expiry date after 1 hr for both the cookies.
      firstName.setMaxAge(60*60); 
      lastName.setMaxAge(60*60); 

      // Add both the cookies in the response header.
      response.addCookie( firstName );
      response.addCookie( lastName );

      // Set response content type
      response.setContentType("text/html");
      //response.sendRedirect("index.html");
      if(login.containsKey(firstN))
      {
          if(login.containsValue(lastN))
          {
      PrintWriter out = response.getWriter();
      out.write("response data");
      String title = "Setting Cookies Example";
      String docType =
      "<!doctype html public \"-//w3c//dtd html 4.0 " +
      "transitional//en\">\n";
      out.println(docType +
                "<html>\n" +
                "<head><title>" + title + "</title></head>\n" +
                "<body bgcolor=\"#f0f0f0\">\n" +
                "<h1 align=\"center\">" + title + "</h1>\n" +
                "<ul>\n" +
                "  <li><b>First Name</b>: "
                + request.getParameter("first_name") + "\n" +
                "  <li><b>Last Name</b>: "
                + request.getParameter("last_name") + "\n" +
                "</ul>\n" +
                "</body></html>");
          }
          else
            response.sendRedirect("login.html");
      }
          else
            response.sendRedirect("login.html");
        }
        finally {
            out1.close();
        }*/
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
        public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

    
}