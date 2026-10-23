public class Pokemon {
    private String nome;
    private String tipo;
    private String nature;

    public Pokemon(String nome, String tipo, String nature){
        this.nome = nome;
        this.tipo = tipo;
        this.nature = nature;
    }

    public String getNome() { return nome; }
    public String getTipo() { return tipo; }
    public String getNature() { return nature; }

    public void monstrarInfo() {
        System.out.println("- Nome: " + nome + "Tipo: " + tipo + "Nature: " + nature );

    }
}
