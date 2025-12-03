 function closeModal() {
            window.location.href = '/'; // Redireciona para a tela index
        }

        // Fechar modal ao clicar fora dele
        document.querySelector('.modal-overlay').addEventListener('click', function(e) {
            if (e.target === this) {
                closeModal();
            }
        });

        // Fechar modal com a tecla ESC
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeModal();
            }
        });