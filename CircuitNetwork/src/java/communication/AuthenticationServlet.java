package communication;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import static java.lang.Compiler.command;
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
        
          
            //create a new cookie named authenticate with value authenticated
            String user = request.getParameter("user");
            Cookie authenticateCookie = new Cookie("authenticate", user);
            //set the age of the cookie
            authenticateCookie.setMaxAge(60 * 60); //cookie lasts for an hour
            //add cookie to responsej
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
        PrintWriter out = response.getWriter();
       
        try {
           
           //to get the controller running 
           String user = request.getParameter("user");
           ControllerMain currentController;
           
            if (webController.containsKey(user)) {
                currentController = webController.get(user);
                
              
            } 
           
            else {
                //create a new one if it doesn't exist
                String rootPath = this.getServletContext().getRealPath("/"); //CircuitNetwork/build/web/
                //create a new one if it doesn't exist
                currentController = new ControllerMain(rootPath);
                webController.put(user, currentController);
               
                
            }
            
            
            //to get the command value
            String command = request.getParameter("command");
            //to get the data value 
            String string = request.getParameter("data");
           
           //switch for different command values 
           switch (command) {
               case "testPy":
                   {
                      
                       System.out.println(string);
                       String output = currentController.runPython(string); //use method to execute command
                       out.write(output);
                       break;
                   }
               case "execute":
                   {
                       System.out.println(string);
                       String output = currentController.runPython(string); //use method to execute command
                       out.write(output);
                       break;
                   }
               case "kwat":
               {
                   System.out.println(string);
                   String output = currentController.runPython(string); //use method to execute command
                   out.write(output);
                   break;
               }
               
               case "registration":
               {
                   String userName = request.getParameter("userName");
                   String userPassword = request.getParameter("userPassword");
                   String wrongInfo = ("");
                   System.out.println(userName);
                   System.out.println(userPassword);
                   //call on the function passing the userName and userPassword
                   String info = verifyInfo(userName, userPassword, wrongInfo);
                   //for now its the userName
                   out.write(info);
                   break;
               }
               default:
                   System.out.println("help me ");
                   
                   break;
           }

           
        } finally {
            out.close();
        }
        
    }


/*
     *Function: This is where the user credentials verified
     *I will parse the json file's array and check for user
     *If user exists then their value attached to the key will be checked
     *If it matches then the user will be allowed to use the app 
     */
    public String verifyInfo(String userName, String userPassword, String wrongInfo) {
        //if the user is new or not
        boolean newUser = false;
        
        
        JSONParser parser = new JSONParser();

        /*
         *This will parse the json object that contains all the user information 
         */
        try {

            //json data is parsed
            Object userVerification = parser.parse(new FileReader("/Users/valeriysosnovskiy/UCSD_IGEM/CircuitNetwork/web/code.json"));
            System.out.println("all the exisiting information: " + userVerification);

            //json object is created containing the past data 
            JSONObject jsonObject = (JSONObject) userVerification;
            

            //getting the array information, which is the user name 
            //authenticate is the id for the array 
            JSONArray authenticate = (JSONArray) jsonObject.get("authenticate");
           
            //iterating the elements in the array to search for a match 
            Iterator<String> authenticateIterator = authenticate.iterator();
            while (authenticateIterator.hasNext()) {
                //if existing user
                if (userName.equals(authenticateIterator.next())) {
                    if(userPassword.equals(jsonObject.get(userName))){
                        return (userName);
                    }
                    else{
                    wrongInfo = ("Wrong user name or password, please try again");
                    return (wrongInfo);
                    }

                } //if new user
                else {
                   newUser = true;
                    
                }

            }
            
            if(newUser == true){
            //json object that holds username and password
                    JSONObject obj = jsonObject;
                    
                    //user name and password
                    obj.put(userName, userPassword);
                    System.out.println("new user information: " + obj);

                    //placing the user information inside an array to check for existing user later on  
                    JSONArray information = authenticate;
                    information.add(userName);
                    
                    //placing the login and password inside the json object 
                    obj.put("authenticate", information);

                    try {
                        //writing the info to the file code.json 
                        FileWriter file = new FileWriter("/Users/valeriysosnovskiy/UCSD_IGEM/CircuitNetwork/web/code.json");
                        file.write(obj.toJSONString());
                        file.flush();
                        file.close();

                    } catch (IOException e) {
                    }
            }
            else{}
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

        return (userName);
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