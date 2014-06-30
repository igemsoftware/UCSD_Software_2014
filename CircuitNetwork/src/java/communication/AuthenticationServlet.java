package Communication;

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
<<<<<<< HEAD
        try (PrintWriter out = response.getWriter()) {
            String input = request.getParameter("key");
            //String input2 = request.getParameter("password");
               System.out.println(input);
//            response.setContentType("application/json");  
            String responseString = "from the server";
            out.write("{data:"+responseString+"}");
=======
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

    

>>>>>>> e41d1886aed4b0846334431e26ec77206fa7a087

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
        } finally {
            out.close();
        }
    }


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
<<<<<<< HEAD
        //processRequest(request, response);
        // Create cookies for first and last names.      
      Cookie firstName = new Cookie("Login",
                      request.getParameter("first_name"));
      Cookie lastName = new Cookie("Password",
                      request.getParameter("last_name"));

      // Set expiry date after 24 Hrs for both the cookies.
      firstName.setMaxAge(60*60*24); 
      lastName.setMaxAge(60*60*24); 

      // Add both the cookies in the response header.
      response.addCookie( firstName );
      response.addCookie( lastName );

      // Set response content type
      response.setContentType("text/html");
 
      PrintWriter out = response.getWriter();
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
                "  <li><b>Login</b>: "
                + request.getParameter("first_name") + "\n" +
                "  <li><b>Password</b>: "
                + request.getParameter("last_name") + "\n" +
                "</ul>\n" +
                "</body></html>");
=======
        processPostRequest(request, response);
>>>>>>> e41d1886aed4b0846334431e26ec77206fa7a087
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

<<<<<<< HEAD
}
=======
    
}
>>>>>>> e41d1886aed4b0846334431e26ec77206fa7a087
