import edu.princeton.cs.algs4.Digraph;
import java.io.*;

public class WikiAnalyzer {
    public static void main(String[] args) throws IOException {
        int numVertices = 2394385; // Valor do cabeçalho
        Digraph G = new Digraph(numVertices + 1); // +1 por segurança de índice

        BufferedReader br = new BufferedReader(new FileReader("data/WikiTalk.txt"));
        String line;
        
        while ((line = br.readLine()) != null) {
            if (line.startsWith("#")) continue; // Pula comentários
            
            String[] nodes = line.split("\\s+");
            int v = Integer.parseInt(nodes[0]);
            int w = Integer.parseInt(nodes[1]);
            G.addEdge(v, w);
        }

        System.out.println("Grafo carregado com sucesso!");

        System.out.println("Número de vértices: " + G.V());
        System.out.println("Número de arestas: " + G.E());

        double V = G.V();
        double E = G.E();
        double densidade = E / (V * (V - 1));
        System.out.println("Densidade do grafo: " + densidade);

        System.out.println("Iniciando exportação de métricas...");

        try (PrintWriter writer = new PrintWriter(new File("results/metricas_vertices.csv"))) {
            // Cabeçalho do CSV
            writer.println("Vertice;GrauEntrada;GrauSaida");

            for (int v = 0; v < G.V(); v++) {
                int in = G.indegree(v);
                int out = G.outdegree(v);

                // Opcional: só exportar vértices que tiveram alguma atividade
                if (in > 0 || out > 0) {
                    writer.println(v + ";" + in + ";" + out);
                }
        
                // Feedback visual a cada 500k vértices para você não achar que travou
                if (v % 500000 == 0) System.out.println("Processados: " + v);
            }
        } catch (FileNotFoundException e) {
        System.err.println("Erro ao criar o arquivo CSV.");
    }
        System.out.println("Exportação concluída! Verifique o arquivo metricas_vertices.csv");

    }
}
