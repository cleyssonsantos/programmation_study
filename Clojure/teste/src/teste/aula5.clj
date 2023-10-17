(ns teste.aula5)

(def lista1 [1, 2, 3, 4, 5])
(println lista1)

; Apenas praticando o laço "for"
(def nova-lista (map #(* 2 %) lista1))
(println nova-lista)

(def estoque {"Mochila" 10, "Camiseta" 5}) ; Array Map
(println (class estoque))

(println "Temos" (count estoque) "valores.")
(println "As chaves são" (keys estoque))
(println "Os valores são" (vals estoque))

; Não é comum usar str como chave do Array Map.

(def estoque-novo {:mochila 10
                   :camiseta 5})

(println (assoc estoque :cadeira 3))

(println (update estoque-novo :mochila inc))

(println (dissoc estoque-novo :mochila))


(def pedido-map {:mochila  {:quantidade 2, :preco 80}
                 :camiseta {:quantidade 1, :preco 2}})
(println pedido-map)

;Para redefinir o simbolo
(def pedido-map (assoc pedido-map :chaveiro {:quantidade 1, :preco 10}))
(println pedido-map)
(println (pedido-map :mochila))
(println (get pedido-map :mochila))
(println (-> pedido-map :mochila :quantidade)) ;Fiz muito isso na captalys
(println (:cadeira pedido-map {})) ; Um get mais comum de ser usado, com valor default {} caso voltar nil
(println (update-in pedido-map [:mochila :quantidade] inc))