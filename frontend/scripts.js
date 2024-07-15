    // Variáveis
    const table = new DataTable("#myTable", {
      paging: false,
      info: false,
      searching: false,
      columnDefs: [
        { orderable: false, targets: 3 },
        { orderable: false, targets: 4 },
      ],
    });

    let patchID = null;

    // Funções Não-Assínconas
    // Abre Input para criar novo tipo de acão e Botão para fechar o input, se já estiver aberto e com conteúdo, chame a função postTipoAcao()
    function openNewTipoAcao() {
      document.getElementById("inputNewTipoAcao").classList.remove("hidden");
      document
        .getElementById("buttonCloseNewTipoAcao")
        .classList.remove("hidden");

      if (document.getElementById("inputNewTipoAcao").value !== "") {
        postTipoAcao();
      }
    }

    // Fecha o input de criar tipo de ação
    function closeNewTipoAcao() {
      document.getElementById("inputNewTipoAcao").value = "";
      document.getElementById("inputNewTipoAcao").classList.add("hidden");
      document.getElementById("buttonCloseNewTipoAcao").classList.add("hidden");
    }

    // Formata a data para aparecer na tabela
    function formatDateTable(isoDate) {
      const [year, month, day] = isoDate.split("-");
      return `${day}/${month}/${year}`;
    }

    // retorna uma string com o formato de date aceito pela db
    function formatDateDB(isoDate) {
      const day = isoDate.getDate();
      const month = isoDate.getMonth() + 1;
      const year = isoDate.getFullYear();
      const formatedDay = day < 10 ? `0${day}` : day;
      const formatedMonth = month < 10 ? `0${month}` : month;
      return `${year}-${formatedMonth}-${formatedDay}`;
    }

    // Retorna uma string com a data de hoje que é aceita pelo banco de dados
    function todaysDate() {
      const today = new Date();
      return formatDateDB(today);
    }

    // Inseri um atributo que só libera inserir datas a partir da data de hoje
    function setMinDate() {
      let minDate = new Date();
      minDate.setDate(new Date().getDate() + 10);
      let minDateString = formatDateDB(minDate);
      document
        .getElementById("inputDataPrevista")
        .setAttribute("min", minDateString);
    }

    // Inseri um atributo que só libera inserir datas a partir da data de cadastro do item editado
    function setMinDateDB(minDateDB){
      let minDate = new Date();
      minDate.setDate(new Date(minDateDB).getDate() + 11);
      let minDateString = formatDateDB(minDate);
      document
        .getElementById("inputDataPrevista")
        .setAttribute("min", minDateString);
    }

    // Limpa os valores nos inputs
    function clearInputs() {
      document.getElementById("inputDataPrevista").value = "";
      document.getElementById("selectAcao").value = "";
      document.getElementById("inputInvestimentoPrevisto").value = "";
    }

    // Volta para as configurações de adicionar Ação
    function goBack() {
      clearInputs();
      document.getElementById("patchBtn").classList.add("hidden");
      document.getElementById("backBtn").classList.add("hidden");
      document.getElementById("postBtn").classList.remove("hidden");
      document.getElementById("clearBtn").classList.remove("hidden");
    }

    // Funções Assíncronas (Que usam o Banco de Dados)

    // Realiza a busca no banco de dados e adiciona no campo select como option, as opções de tipos de ação
    async function getTiposAcoes() {
      const response = await fetch("http://127.0.0.1:8000/tipos_acao/");
      const data = await response.json();

      Object.keys(data).map((option) => {
        const selectOption = document.createElement("option");
        selectOption.value = data[option].codigo_acao;
        selectOption.textContent = data[option].nome_acao;
        document.getElementById("selectAcao").appendChild(selectOption);
      });
    }

    // Realiza a busca no banco de dados e adiciona as linhas na tabela
    async function getAcoes() {
      const response = await fetch("http://127.0.0.1:8000/acoes/");
      const data = await response.json();

      data.forEach((row) => {
        table.row
          .add([
            row.tipo_acao.nome_acao,
            formatDateTable(row.data_prevista),
            `R$ ${row.investimento.toFixed(2)}`,
            `<div class='text-center'><a onclick='{openEditor(${row.id})}' title='Abre o campo de edição da linha'><span class='glyphicon glyphicon-pencil blueIconTable'></span></a></div>`,
            `<div class='text-center'><a onclick='{deleteRow(${row.id})}' title='Deletar a linha'><span class='glyphicon glyphicon-remove redIconTable'></span></a></div>`,
          ])
          .draw(false);
      });
    }

    // Envia os conteúdos dos inputs para adicionar mais um linha no banco de Acões
    async function postAcao() {
      const investimentoFormated = parseFloat(
        document.getElementById("inputInvestimentoPrevisto").value
      ).toFixed(2);

      const postData = {
        codigo_acao: document.getElementById("selectAcao").value,
        data_prevista: document.getElementById("inputDataPrevista").value,
        data_cadastro: todaysDate(),
        investimento: investimentoFormated,
      };

      try {
        const response = await fetch("http://127.0.0.1:8000/acao/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(postData),
        });

        if (!response.ok) {
          throw new Error("Erro na requisição: " + response.statusText);
        }
        location.reload();
      } catch (e) {
        console.error("Erro: ", e);
      }
    }

    // Envia o conteúdo do input de criar novo tipo de ação
    async function postTipoAcao() {
      const postData = {
        nome_acao: document.getElementById("inputNewTipoAcao").value,
      };

      try {
        const response = await fetch("http://127.0.0.1:8000/tipo_acao/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(postData),
        });

        if (!response.ok) {
          throw new Error("Erro na requisição: " + response.statusText);
        }
        location.reload();
      } catch (e) {
        console.error("Erro: ", e);
      }
    }

    // Atualiza os dados segundo a ID fornecida com os valores dos inputs
    async function patchAcao(id) {
      const patchData = {
        codigo_acao: document.getElementById("selectAcao").value,
        data_prevista: document.getElementById("inputDataPrevista").value,
        investimento: document.getElementById("inputInvestimentoPrevisto")
          .value,
      };
      try {
        const response = fetch(`http://127.0.0.1:8000/acao/${id}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(patchData),
        });
        location.reload();
      } catch (e) {
        console.error(e);
      }
    }

    // Deleta a linha selecionada pelo ID
    async function deleteRow(id) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/acao/${id}`, {
          method: "DELETE",
        });
        location.reload();
      } catch (e) {
        console.error(e);
      }
    }

    // Mostra os botões para editar a ação selecionada, esconde os botões de adicionar nova ação e colocar os valores da ação selecionada nos inputs
    async function openEditor(id) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/acao/${id}`);
        const data = await response.json();
        patchID = id;
        document.getElementById("patchBtn").classList.remove("hidden");
        document.getElementById("backBtn").classList.remove("hidden");
        document.getElementById("postBtn").classList.add("hidden");
        document.getElementById("clearBtn").classList.add("hidden");
        document.getElementById("inputDataPrevista").value = data.data_prevista;
        document.getElementById("selectAcao").value =
          data.tipo_acao.codigo_acao;
        document.getElementById("inputInvestimentoPrevisto").value =
          data.investimento;
        setMinDateDB(data.data_cadastro);
      } catch (e) {
        console.error(e);
      }
    }

    // Iniciadoras de Funções

    setMinDate(); // A data mínima é de 10 dias a partir da data de cadastro
    getAcoes(); // <table>
    getTiposAcoes(); // <select>