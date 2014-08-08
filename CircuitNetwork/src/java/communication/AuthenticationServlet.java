package communication;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Iterator;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
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
        
        
        if(password.equals("welcome")){
            
        System.out.println("Welcome to iGEM");
        System.out.println("<br>Welcome," + user);
        //create a new cookie named authenticate with value authenticated
        Cookie authenticateCookie = new Cookie( "user" , "password");
        //add cookie once clicked on the login 
        response.addCookie(authenticateCookie);
        //set the age of the cookie
        //set the age to two hours        
        authenticateCookie.setMaxAge(60 * 120);
        //set to the next page
        
        out.println("Cookies have been added");
        response.sendRedirect("Demo_Site_Login");
        
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
        
        System.out.println("Logged out");
        
        

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
        PrintWriter out = response.getWriter();
        
        String commandString = request.getParameter("command");
        
        System.out.println(commandString);
        String result = executeCommand(commandString);
        out.write(result);
        //added to close the print writer
        out.close();

        //String obtainFile = request.getParameter("filed");
        //System.out.println(obtainFile);
        
        //String showFile = createFile(String obtainFile);
        //out.write(showFile);
        out.close();
    }
    //@SuppressWarnings("unchecked")
    public static void createFile(){
        JSONObject obj = new JSONObject();
         
        JSONArray nodes = new JSONArray();
	nodes.add("5 -> 9 -> 4");
	nodes.add("5 -> 4");
	nodes.add("5 -> 2 -> 2");
	nodes.add("5 -> 2");
	nodes.add("1 -> 4 -> 1");
	nodes.add("1 -> 1");
	nodes.add("6 -> 7 -> 6");
	nodes.add("6 -> 6");
	nodes.add("6 -> 9 -> 1");
	nodes.add("6 -> 1");
	nodes.add("6 -> 10 -> 5");
	nodes.add("6 -> 5");
	nodes.add("10 -> 8 -> 7");
	nodes.add("10 -> 7");
	
 
	obj.put("digraph", nodes);
  
	try {

            FileWriter file = new FileWriter("text.json");
            file.write(obj.toJSONString());
            System.out.println("JSON object:" + obj);
            file.flush();
            file.close();
            parsingJSON();
 
	} catch (IOException e) {
		e.printStackTrace();
	}
        
        
        
        
        
        
    }
    private static void parsingJSON(){
        JSONParser parser = new JSONParser();
        try{
            Object obj = parser.parse(new FileReader("text.json"));
            JSONObject jsonObject = (JSONObject) obj;
            
          
            JSONArray nodes = (JSONArray) jsonObject.get("digraph");
            
            System.out.println("nodes:" + nodes );
            Iterator<String> iterator = nodes.iterator();
            while(iterator.hasNext()){
                System.out.println(iterator.next());
            }
            
        }catch (Exception e){
            e.printStackTrace();
        }
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
