(ns loja.db)

(def pedido-1
  {:usuario 15, 
   :itens {:mochila {:id :mochila, :quantidade 2, :preco-unitario 80},
           :camiseta {:id :camiseta, :quantidade 3, :preco-unitario 40},
           :tenis {:id :tenis, :quantidade 1}}})

(def pedido-2
  {:usuario 11,
   :itens {:mochila {:id :mochila, :quantidade 2, :preco-unitario 80},
           :camiseta {:id :camiseta, :quantidade 3, :preco-unitario 40},
           :tenis {:id :tenis, :quantidade 1}}})

(def pedido-3
  {:usuario 3,
   :itens {:mochila {:id :mochila, :quantidade 2, :preco-unitario 80},
           :camiseta {:id :camiseta, :quantidade 3, :preco-unitario 40},
           :tenis {:id :tenis, :quantidade 1}}})

(def pedido-4
  {:usuario 7,
   :itens {:mochila {:id :mochila, :quantidade 2, :preco-unitario 80},
           :camiseta {:id :camiseta, :quantidade 3, :preco-unitario 40},
           :tenis {:id :tenis, :quantidade 1}}})

(defn todos-os-pedidos []
  [pedido-1 pedido-2 pedido-3 pedido-4])
