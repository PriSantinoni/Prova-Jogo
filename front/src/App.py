import { useEffect, useState } from 'react';

// O Nginx do container encaminha /api/* para http://api:3000/* (DNS interno do Compose)
const API_URL = '/api/produtos';

const estilos = {
  pagina: { fontFamily: 'system-ui, sans-serif', maxWidth: 900, margin: '40px auto', padding: '0 16px' },
  tabela: { width: '100%', borderCollapse: 'collapse' },
  th: { textAlign: 'left', padding: 10, background: '#1f2937', color: '#fff' },
  td: { padding: 10, borderBottom: '1px solid #e5e7eb' },
};

export default function App() {
  const [produtos, setProdutos] = useState([]);
  const [carregando, setCarregando] = useState(true);
  const [erro, setErro] = useState(null);

  async function carregar() {
    setCarregando(true);
    setErro(null);
    try {
      const resp = await fetch(API_URL);
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      setProdutos(await resp.json());
    } catch (e) {
      setErro(e.message);
    } finally {
      setCarregando(false);
    }
  }

  useEffect(() => {
    carregar();
  }, []);

  return (
    <div style={estilos.pagina}>
      <h1>Produtos</h1>
      <button onClick={carregar}>Atualizar</button>

      {carregando && <p>Carregando...</p>}
      {erro && <p style={{ color: 'crimson' }}>Erro ao buscar dados: {erro}</p>}

      {!carregando && !erro && (
        <table style={{ ...estilos.tabela, marginTop: 16 }}>
          <thead>
            <tr>
              <th style={estilos.th}>ID</th>
              <th style={estilos.th}>Nome</th>
              <th style={estilos.th}>Descrição</th>
              <th style={estilos.th}>Preço</th>
            </tr>
          </thead>
          <tbody>
            {produtos.length === 0 ? (
              <tr>
                <td style={estilos.td} colSpan={4}>Nenhum produto cadastrado.</td>
              </tr>
            ) : (
              produtos.map((p) => (
                <tr key={p.id}>
                  <td style={estilos.td}>{p.id}</td>
                  <td style={estilos.td}>{p.nome}</td>
                  <td style={estilos.td}>{p.descricao}</td>
                  <td style={estilos.td}>
                    {Number(p.preco).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      )}
    </div>
  );
}
