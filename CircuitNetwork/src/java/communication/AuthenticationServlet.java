
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
            System.out.println(command);
           
           //switch for different command values 
           switch (command) {
               case "query":
               {
                   //to get the data value 
                   System.out.println("query");
                   String query = request.getParameter("data");
                   String output = currentController.executeQuery(query); //use method to execute command
                   out.write(output);
                   break;
               }
               
               case "register":
               {
                   //to get the data value 
                   System.out.println("server reached");
                   String userName = request.getParameter("name");
                   String userPassword = request.getParameter("email");
                   String wrongInfo = ("");
                   System.out.println("userName: " + userName);
                   System.out.println("userPassword: "+ userPassword);
                   //call on the function passing the userName and userPassword
                   String info = registerInfo(userName, userPassword, wrongInfo);
                   
                   //for now its the userName
                   out.write(info);
                  
                   break;
               }
               case "login":
               {
                   //to get the data value 
                   System.out.println("server reached");
                   String userName = request.getParameter("name");
                   String userPassword = request.getParameter("email");
                   String wrongInfo = ("");
                   System.out.println("userName: " + userName);
                   System.out.println("userPassword: "+ userPassword);
                   //call on the function passing the userName and userPassword
                   String info = registeredUser(userName, userPassword, wrongInfo);
                   
                   //for now its the userName
                   out.write(info);
                   break;
               }
               case "contactUs":
               {
                   //to get the data value 
                   String name = request.getParameter("name");
                   String email = request.getParameter("email");
                   String affiliation = request.getParameter("affiliation");
                   String message = request.getParameter("message");
                   
                   GoogleMail googleMail;
                   googleMail = new GoogleMail(name, email, affiliation, message);
                   
               }
               case "uploadNew":
               {
                    String upload = request.getParameter("data");
                    String output = currentController.executeUpload(upload);
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
     *Function: This is where the user information is registered
     *I will parse the json file's array and check for user
     *If user exists then they have to resubmit another username 
     *If no match, then user information is stored in code.json 
     */
    public String registeredUser(String userName, String userPassword, String wrongInfo) {
        //if the user is new or not
        boolean existingUser = false;
        String enteredUser = userName;
        String enteredPassword = userPassword;
        
        JSONParser parser = new JSONParser();
        String rootPath = this.getServletContext().getRealPath("/"); //CircuitNetwork/build/web/
        /*
         *This will parse the json object that contains all the user information 
         */
        try {

            //json data is parsed
            Object userVerification = parser.parse(new FileReader(rootPath + "code.json"));
            
            
            System.out.println(userVerification);
            System.out.println("all the exisiting information: " + userVerification);

            //json object is created containing the past data 
            JSONObject jsonObject = (JSONObject) userVerification;
            

            //getting the array information, which is the user name 
            //authenticate is the id for the array 
            JSONArray authenticate = (JSONArray) jsonObject.get("authenticate");
            System.out.println("Items in the array: " + authenticate);
            //iterating the elements in the array to search for a match 
            Iterator<String> authenticateIterator = authenticate.iterator();
            while (authenticateIterator.hasNext()) {
                //if existing user
                if (enteredUser.equals(authenticateIterator.next())) {
                    existingUser = true;
                    
                    
                    
                }
                     
                
                else {
                      wrongInfo = ("Wrong userName/password");
                      return (wrongInfo);
                    
                }
     
            }
            if(existingUser == true){
               String validator = (String) jsonObject.get(enteredUser);
               if(enteredPassword.equals(validator)){
                   wrongInfo = ("Welcome");
                      return (wrongInfo);
               }
               else{
                wrongInfo = ("Username or password incorrect, please try again");
                      return (wrongInfo);
               }
               
            }
            
            
           
         } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
       //existingUser = false;
       return (enteredUser);
    }
    
    public String registerInfo(String userName, String userPassword, String wrongInfo) {
        //if the user is new or not
        boolean newUser = false;
        String enteredUser = userName;
        String enteredPassword = userPassword;
        
        JSONParser parser = new JSONParser();
         String rootPath = this.getServletContext().getRealPath("/"); //CircuitNetwork/build/web/
        /*
         *This will parse the json object that contains all the user information 
         */
        try {

            //json data is parsed
            Object userVerification = parser.parse(new FileReader(rootPath + "code.json"));
            
            System.out.println(userVerification);
            System.out.println("all the exisiting information: " + userVerification);

            //json object is created containing the past data 
            JSONObject jsonObject = (JSONObject) userVerification;
            

            //getting the array information, which is the user name 
            //authenticate is the id for the array 
            JSONArray authenticate = (JSONArray) jsonObject.get("authenticate");
            System.out.println("Items in the array: " + authenticate);
            //iterating the elements in the array to search for a match 
            Iterator<String> authenticateIterator = authenticate.iterator();
            while (authenticateIterator.hasNext()) {
                //if existing user
                if (enteredUser.equals(authenticateIterator.next())) {
                    wrongInfo = ("User already exists");
                    return (wrongInfo);
                    
                }
                     
                //if new user
                else {
                   newUser = true;
                    
                }

            }
            
            if(newUser == true){
            //json object that holds username and password
                    JSONObject obj =  jsonObject;
                    
                    //user name and password
                    obj.put(enteredUser, enteredPassword);
                    System.out.println("new user information: " + obj);

                    //placing the user information inside an array to check for existing user later on  
                    JSONArray information = authenticate;
                    information.add(enteredUser);
                    
                    //placing the login and password inside the json object 
                    obj.put("authenticate", information);

                    try {
                       
                        //writing the info to the file code.json 
                        FileWriter file = new FileWriter(rootPath + "code.json");
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

        return (enteredUser);
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