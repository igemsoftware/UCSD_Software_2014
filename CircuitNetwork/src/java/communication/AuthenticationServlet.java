package communication;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.*;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.lang.Object;
import org.json.simple.JSONObject; 
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
        JSONObject obj = new JSONObject();
        String user = request.getParameter("key");
        PrintWriter out = response.getWriter();
        try {
            out.println(user);//("data from the server");
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
