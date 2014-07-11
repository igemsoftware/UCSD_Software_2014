package communication;

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
import java.io.InputStreamReader;
import java.io.OutputStream;

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
            String user = request.getParameter("user");
            String password = request.getParameter("password");

//            create a new cookie named authenticate with value authenticated
            Cookie authenticateCookie = new Cookie("authenticate", "authenticated");
//            set the age of the cookie
            authenticateCookie.setMaxAge(60 * 60); //cookie lasts for an hour
//            add cookie to responsej
            response.addCookie(authenticateCookie);
            
    }
    
    

    
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
         

        
        //redirect the page to another page (can call for login button)
//        response.sendRedirect("index.html");
        PrintWriter out = response.getWriter();
      
           
           String line = null;
           System.out.print("Type in your command");
           
           //wraps the BufferedReader around the InputStreamReader
           //Reads text from a character-input stream, buffering characters 
           //so as to provide for the efficient reading of characters, arrays, and lines.
           BufferedReader readMe = new BufferedReader(new InputStreamReader(System.in));
           try{
                
                //reads the line from the command line
                line = readMe.readLine();
               
                /*provides methods for performing input from the process, 
                 *performing output to the process, waiting for the process to 
                 *complete, checking the exit status of the process, 
                 *and destroying (killing) the process.
                 */
                Process process = Runtime.getRuntime().exec(line);
            //Returns the output stream connected to the normal input of the subprocess
            OutputStream outputStream = process.getOutputStream();
            out.write(outputStream.toString());
               
                 } catch (IOException ioe) {
         System.out.println("Error Error");
         System.exit(1);
            }
            
            //close the reader 
            readMe.close();
            System.out.println("Thank you ");
        
        
      out.write("Good things happened");
       
       

       
       
        
        
       
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
        protected void doGet(HttpServletRequest request, HttpServletResponse response )
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

    
}
