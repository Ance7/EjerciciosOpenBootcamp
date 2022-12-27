//Para practicar la encapsulación:

//Crear clase Persona.

//Crear variables las privadas edad, nombre y telefono de la clase Persona.

//Crear gets y sets de cada propiedad.

//Crear un objeto persona en el main.

//Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.

public class ejercicio3 {
    public static void main (String[] args){
    
    Persona Sujeto = new Persona();
    Sujeto.setEdad(23);
    Sujeto.setNombre("Juan");
    Sujeto.setTelefono(12345678);

    System.out.println(Sujeto.getEdad());
    System.out.println(Sujeto.getNombre());
    System.out.println(Sujeto.getTelefono());
    }
}

class Persona {
    private int edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }

    public void setTelefono(int telefono){
        this.telefono = telefono;
    }
    public int getTelefono(){
        return this.telefono;
    }
}