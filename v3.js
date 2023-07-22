const express = require("express");
const sql = require("mssql/msnodesqlv8");
const { Sequelize, DataTypes } = require("sequelize");

// Objet de configuration pour la connexion à la base de données
const config = {
  server: "LAPTOP-TDNN94VH",
  database: "PiSecurityDB",
  driver: "msnodesqlv8",
  options: {
    trustedConnection: true,
  },
};

// Créez une instance Sequelize pour interagir avec la base de données
let sequelize;

try {
  sequelize = new Sequelize(config.database, null, null, {
    dialect: "mssql",
    dialectModule: sql, // Utilisez le pilote "msnodesqlv8"
    dialectOptions: config.options,
  });
  console.log("connecter a la base de donnée");
} catch (error) {
  console.error("Erreur lors de la connexion à la base de données :", error);
  process.exit(-1); // Quitte le processus Node.js avec un code d'erreur (-1)
}

const Element = sequelize.define("Element", {
  zone1: {
    type: DataTypes.CHAR(10),
    allowNull: true,
  },
  zone2: {
    type: DataTypes.CHAR(10),
    allowNull: true,
  },
  zone3: {
    type: DataTypes.CHAR(10),
    allowNull: true,
  },
  zone4: {
    type: DataTypes.CHAR(10),
    allowNull: true,
  },
  statut: {
    type: DataTypes.INTEGER,
    allowNull: true,
  },
});

const app = express();
app.use(express.json());

// Route pour insérer des données dans la base de données
app.post("/insert", (req, res) => {
  const { zone1, zone2, zone3, zone4, statut } = req.body;

  Element.create({ zone1, zone2, zone3, zone4, statut })
    .then((newElement) => {
      console.log("Nouvel élément inséré :", newElement.toJSON());
      res.json(newElement);
    })
    .catch((error) => {
      console.error("Erreur lors de l'insertion de l'élément :", error);
      res
        .status(500)
        .json({ error: "Erreur lors de l'insertion de l'élément" });
    });
});

app.get("/elements", (req, res) => {
  Element.findAll()
    .then((elements) => {
      console.log("All elements retrieved successfully:");
      elements.forEach((element) => {
        console.log(element.toJSON());
      });
      res.json(elements);
    })
    .catch((error) => {
      console.error("Error while retrieving elements:", error);
      res.status(500).json({ error: "Error while retrieving elements" });
    });
});
const port = 3000;
app.listen(port, () => {
  console.log(`Le serveur est en cours d'exécution sur le port ${port}.`);
});
