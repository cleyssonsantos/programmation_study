(ns teste.aula6)

(def pedido {:mochila  {:quantidade 2, :preco 80}
             :camiseta {:quantidade 3, :preco 40}})

(defn imprime-e-15 [valor]
  (println "valor" valor)
  15)

(println (map imprime-e-15 pedido))

(defn imprime-e-15-novo [[chave valor]]
  (println chave "e" valor)
  15)

(println (map imprime-e-15-novo pedido))

(def pedido {:mochila  {:quantidade 2, :preco 80}
             :camiseta {:quantidade 3, :preco 40}})

(defn soma-pedido [[chave valor]]
  (let [quantidade (-> valor :quantidade)
        preco (-> valor :preco)]
    (* quantidade preco)))

(println (map soma-pedido pedido))

(defn soma-pedido [[_ valor]] ; O _ significa que tem alguem ali mas nao vou usar, estou fazendo um distroct, entao dane-se o argumento "parametro" ali
  (let [quantidade (-> valor :quantidade)
        preco (-> valor :preco)]
    (* quantidade preco)))

 ;THREAD LAST -> Vai deixar a coleção passando como ultimo parametro. Se usar o first vai dar erro, porque no first usa coleção em primeiro, e funcao no ultimo parametro.
(defn total-do-pedido
  [pedido]
  (->> pedido
      (map soma-pedido ,,,)
      (reduce + ,,,)))

(println (total-do-pedido pedido))

(defn preco-total-do-produto [produto]
  (* (:quantidade produto) (:preco produto)))

;THREAD LAST dnv
(defn total-do-pedido
  [pedido]
  (->> pedido
       vals
       (map preco-total-do-produto)
       (reduce +)))

(println (total-do-pedido pedido))


;------------------------------------------------
;Filtrando Mapas e Criando Composições com COMP
(def pedido {:mochila  {:quantidade 2, :preco 80}
             :camiseta {:quantidade 3, :preco 40}
             :chaveiro {:quantidade 1}})

(defn gratuito?
  [item]
  ;(println item)
  (<= (get item :preco 0) 0))

(println "Filtrando gratuitos")
(println (filter gratuito? (vals pedido)))




(defn gratuito?
  [[_ item]]
  (<= (get item :preco 0) 0))

(println "Filtrando gratuitos")
(println (filter gratuito? pedido))




(defn gratuito?
  [item]
  (<= (get item :preco 0) 0))

(println "Filtrando gratuitos")
(println (filter (fn [[chave item]] (gratuito? item)) pedido))

(println (filter #(gratuito? (second %)) pedido))


(defn pago?
  [item]
  (not (gratuito? item)))

(println (pago? {:preco 50}))
(println (pago? {:preco 0}))

(println ((comp not gratuito?) {:preco 50}))

(def pago? (comp not gratuito?))
(println (pago? {:preco 50}))
(println (pago? {:preco 0}))