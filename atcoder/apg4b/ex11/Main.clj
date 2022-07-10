;; (require '[clojure.string :as str])
(use '[clojure.string :refer [split]])


(split "1+1+1-1" #"1")


(let [input "1+1+1-1"
      [plus minus] ((juxt (fn [i] (count (filter #(= % \+) i)))
                          (fn [i] (count (filter #(= % \-) i)))) input)]
  (count (filter #(= % \+) input)))


(defn create-input
  [arg]
  (->> (split arg #" ")
       (apply (fn [op v] (list op (Integer/parseInt v))))))


(def sum #'+)
(def dif #'-)
(def mul #'*)


(defn div
  [a b]
  (if (= b 0)
    "error"
    (quot a b)))


(defn operation
  [n a b]
  (cond
    (= "+" n) (sum a b)
    (= "-" n) (dif a b)
    (= "*" n) (mul a b)
    (= "/" n) (div a b)
    :else "error"))


;; 末尾再帰じゃないのでloop/recurのほうがパフォーマンスはよいだろうな
;; それかreduceを使うのが良さそうだけど。途中で停止できないのがreduceだとアウト
;; いや計算するところと出力するところをわければよい
(defn lo
  [col init cnt]
  (if (= (count col) 0)
    init
    (let [[op value] (first col)
          new-value (operation op init value)]
      (if (= new-value "error")
        (println new-value)
        (do
          (println (str cnt ":" new-value))
          (recur (rest col) new-value (inc cnt)))))))


(let [first (Integer/parseInt (read-line))
      second (Integer/parseInt (read-line))
      ops (map (fn [_] (create-input (read-line))) (range first))]
  (lo ops second 1))

