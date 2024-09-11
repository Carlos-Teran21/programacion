/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package clases;

import java.awt.List;
import java.util.ArrayList;

/**
 *
 * @author Biblioteca
 */
public class personas {
    private String Nombre;
    private String Apellido;
    private String Direccion;
    private String Edad;
    
 public personas(String Nombre,String Apellido,String Direccion,String Edad){
    this.Nombre = Nombre;
    this.Apellido = Apellido;
    this.Direccion = Direccion;
    this.Edad = Edad;
    
 }   

    /**
     * @return the Nombre
     */
    public String getNombre() {
        return Nombre;
    }

    /**
     * @param Nombre the Nombre to set
     */
    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    /**
     * @return the Apellido
     */
    public String getApellido() {
        return Apellido;
    }

    /**
     * @param Apellido the Apellido to set
     */
    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }

    /**
     * @return the Direccion
     */
    public String getDireccion() {
        return Direccion;
    }

    /**
     * @param Direccion the Direccion to set
     */
    public void setDireccion(String Direccion) {
        this.Direccion = Direccion;
    }

    /**
     * @return the Edad
     */
    public String getEdad() {
        return Edad;
    }

    /**
     * @param Edad the Edad to set
     */
    public void setEdad(String Edad) {
        this.Edad = Edad;
    }
    
    public ArrayList<String> lista(){
         ArrayList<String> Lista= new ArrayList();
         Lista.add(0,getNombre());
         Lista.add(1,getApellido());
         Lista.add(2,getDireccion());
         Lista.add(3,getEdad());
         
         
         return null;
    }
       
        
        
    
    }
   

