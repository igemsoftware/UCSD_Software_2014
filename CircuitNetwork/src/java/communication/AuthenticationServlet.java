<<<<<<< HEAD
package communication;
<<<<<<< HEAD
=======

>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
=======
package Communication;
>>>>>>> 59621eb10f54c81510823bd092406573a4747282

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
<<<<<<< HEAD
<<<<<<< HEAD
import java.io.InputStreamReader;
import java.io.OutputStream;
=======
import java.lang.Object;
import java.net.URL;
import java.nio.ByteBuffer;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;
import java.nio.channels.WritableByteChannel;
//import org.json.simple.JSONObject; 
>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
=======
>>>>>>> 59621eb10f54c81510823bd092406573a4747282

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
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
        
        //get json data parameters sent by client
        //the user and password id's of the login page 
        String user = request.getParameter("user");
        String password = request.getParameter("password");
<<<<<<< HEAD
        response.sendRedirect("Demo_Site_Login.html");
        //System.out.println(user);
        //System.out.println(password);
        out.write("authentication processed");
        
        if(password.equals("welcome")){
            out.write("Welcome to iGEM");
            out.write("<br>Welcome," + user);
        //create a new cookie named authenticate with value authenticated
        Cookie authenticateCookie = new Cookie("authenticate", "authenticated");
=======
        
        
        if(password.equals("welcome")){

=======
>>>>>>> 59621eb10f54c81510823bd092406573a4747282
            //get json data parameters sent by client
            String user = request.getParameter("user");
            String password = request.getParameter("password");

//            create a new cookie named authenticate with value authenticated
            Cookie authenticateCookie = new Cookie("authenticate", "authenticated");
//            set the age of the cookie
            authenticateCookie.setMaxAge(60 * 60); //cookie lasts for an hour
//            add cookie to responsej
            response.addCookie(authenticateCookie);
            
<<<<<<< HEAD
        System.out.println("Welcome to iGEM");
        System.out.println("<br>Welcome," + user);
        //create a new cookie named authenticate with value authenticated
        Cookie authenticateCookie = new Cookie( "user" , "password");
>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
        //add cookie once clicked on the login 
        response.addCookie(authenticateCookie);
        //set the age of the cookie
        //set the age to two hours        
        authenticateCookie.setMaxAge(60 * 120);
        //set to the next page
<<<<<<< HEAD
         
=======
        
        out.println("Cookies have been added");
        response.sendRedirect("Demo_Site_Login");
        
>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
        }
        
        else{
            out.print("password or username error");
            response.sendRedirect("Demo_Site.html");
        }
        
        out.close();
<<<<<<< HEAD

        //log out portion
        String LogOut = request.getParameter("LogOut");    
        Cookie authenticateCookie = new Cookie("authenticate", "authenticated");
        authenticateCookie.setMaxAge(-1);
        response.addCookie(authenticateCookie);
        
        out.print("Logged out");
        
        

    }

=======
        
    }

>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
    /*
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

<<<<<<< HEAD
        //redirect the page to another page (can call for login button)
//        response.sendRedirect("Demo_Site.html");
        PrintWriter out = response.getWriter();
=======
        //response.sendRedirect("index.html");
        //JSONObject obj = new JSONObject();
        String user = request.getParameter("key");
=======
    }

    

>>>>>>> 59621eb10f54c81510823bd092406573a4747282

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
        response.sendRedirect("index.html");
        PrintWriter out = response.getWriter();
<<<<<<< HEAD
        
>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
        String commandString = request.getParameter("command");
        
        System.out.println(commandString);
        String result = executeCommand(commandString);
        out.write(result);
<<<<<<< HEAD

    }

    private static String executeCommand(String command) {

        StringBuffer output = new StringBuffer();

        Process p;
        try {
=======
        //added to close the print writer
        out.close();

        //String obtainFile = request.getParameter("filed");
        //System.out.println(obtainFile);
        
        //String showFile = createFile(String obtainFile);
        //out.write(showFile);
        out.close();
    }
    //@SuppressWarnings("unchecked")
 
    private static String executeCommand(String command) {

        StringBuffer output = new StringBuffer();   

        Process p;
        try {

>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
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
<<<<<<< HEAD
        }

        return output.toString();

=======

            
        }finally {
            System.out.close();

        }

        return output.toString();
        
>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
=======
        try {
        } finally {
            out.close();
        }
>>>>>>> 59621eb10f54c81510823bd092406573a4747282
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
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
        public String getServletInfo() {
        return "Short description";
<<<<<<< HEAD
<<<<<<< HEAD
    }// </editor-fold>

}



/*String text = "digraph{\n{rank=same; \nPIGEON_START\n\"a\"\no A 9\np pBad 4\no B 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"b\"\no B 9\nr a 5\no C 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"c\"\no C 9\nc tetR 8\no D 9\n# Arcs\nPIGEON_END\nPIGEON_START\n\"d\"\no D 9\nt a 6\no E 9\n# Arcs\nPIGEON_END\n}\n\n\"bc\" [shape=point, width=0.14159];\n\"bcd\" [shape=point, width=0.14159];\n\"bba\" [shape=point, width=0.14159];\nPIGEON_START\n\"abcd\"\no A 9\np pBad 4\no B 9\nr a 5\no C 9\nc tetR 8\no D 9\nt a 6\no E 9\n# Arcs\nPIGEON_END\n\n\"b\"->\"bc\" [label=\"3\", arrowhead=\"none\"];\n\"c\"->\"bc\" [label=\"3\", arrowhead=\"none\"];\n\"bc\"->\"bcd\" [label=\"3\", arrowhead=\"none\"];\n\"d\"->\"bcd\" [label=\"3\", arrowhead=\"none\"];\n\"a\"->\"bba\" [label=\"3\", arrowhead=\"none\"];\n\"bcd\"->\"bba\" [label=\"3\", arrowhead=\"none\"];\n\"bba\"->\"abcd\";\n\n\"bc\"->\"bc\" [taillabel=\"3 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\"bcd\"->\"bcd\" [taillabel=\"6 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\"abcd\"->\"abcd\" [taillabel=\"9 Days\",labelangle=330, labeldistance=3,\nlabelfontcolor=\"red\", color=transparent];\n\n}\n";
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
            fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);*/
=======
    }// </editor-fold>
>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
=======
    }// </editor-fold>

    
}
>>>>>>> 59621eb10f54c81510823bd092406573a4747282
