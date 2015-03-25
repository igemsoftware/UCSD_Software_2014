package communication;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Iterator;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import java.io.FileWriter;
import java.io.IOException;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;


import communication.WeyekinPoster;
import communication.PigeonToPNG;

/**
 *
 * @author Valeriy
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
        PrintWriter out = response.getWriter();

        try {

            //to get the controller running 
            String user = request.getParameter("user");
            ControllerMain currentController;

            if (webController.containsKey(user)) {
                currentController = webController.get(user);

            } else {
                //create a new one if it doesn't exist
                String rootPath = this.getServletContext().getRealPath("/"); //CircuitNetwork/build/web/
                //create a new one if it doesn't exist
                currentController = new ControllerMain(rootPath);
                webController.put(user, currentController);

            }

            //to get the command value
            String command = request.getParameter("command");
            System.out.println("HELLO THIS IS WHAT IT IS");
            System.out.println(command);

            //switch for different command values 
            switch (command) {
                case "query": {
                    //to get the data value 
                    System.out.println("query");
                    String query = request.getParameter("data");
                    String output = currentController.executeQuery(query); //use method to execute command
                    out.write(output);
                    break;
                }

               
                
                case "contactUs": {
                    //to get the data value 
                    String name = request.getParameter("name");
                    String email = request.getParameter("email");
                    String subject = request.getParameter("subject");
                    String message = request.getParameter("message");
                    
                    GoogleMail googleMail = new GoogleMail(name, email, subject, message);
                    String output= googleMail.writeMessage();
                    out.write(output);
                    break;

                }
                case "uploadNew": {
                    String upload = request.getParameter("data");
                    String output = currentController.executeUpload(upload);
                    out.write(output);

                    break;
                }
                default:
                    System.out.println("help me ");
            }

        } finally {
            out.close();
        }

    }
  
    
   

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
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
     * Handles the HTTP <code>POST</code> method.
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
    }// </editor-fold>
    
    private HashMap<String, ControllerMain> webController = new HashMap();
}
