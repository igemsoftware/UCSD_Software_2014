package communication;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import static java.lang.Compiler.command;
import java.util.HashMap;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


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
        /*
          
            //create a new cookie named authenticate with value authenticated
            String user = request.getParameter("user");
            Cookie authenticateCookie = new Cookie("authenticate", user);
            //set the age of the cookie
            authenticateCookie.setMaxAge(60 * 60); //cookie lasts for an hour
            //add cookie to responsej
            response.addCookie(authenticateCookie);
          */  
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
       response.sendRedirect("index.html");
        
        PrintWriter out = response.getWriter();
       
        try {
            
           //retrieve the users controller object
            String user = request.getParameter("user");
            ControllerMain currentController;
            
            if (webController.containsKey(user)) {
                currentController = webController.get(user);
            } else {
                String rootPath = this.getServletContext().getRealPath("/"); //CircuitNetwork/build/web/
                //create a new one if it doesn't exist
                currentController = new ControllerMain(rootPath);
                webController.put(user, currentController);
            }
            String command = request.getParameter("command"); //parameter from the client
            
            if (command.equals("execute")) {
                String data = request.getParameter("data"); //get data from the request; remember this is packaged into a json object
                //String output = currentController.executeCommand(data); //use method to execute command
                String output = currentController.runPython(data); //use method to execute command
                out.write(output); //write output of command into response for get/pull request
            
            }
         
            String executePy = request.getParameter("command");
            
            if(executePy.equals("pythonPy")){
                String pythonPy  = "Test.py"; //
                String output = currentController.runPython(pythonPy); //use method to execute command
                out.write(output); 
                
            }
            
             } catch (Exception e) {
            e.printStackTrace();

           
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