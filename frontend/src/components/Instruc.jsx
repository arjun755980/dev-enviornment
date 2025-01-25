import '../styles/Instruc.css';

export default function Instruc() {
  return (
    <div className="ascii-container">
      <pre className="ascii-art">
        {`
             /$$               /$$                        /$$$$$$ 
            | $$              | $$          /$$          /$$__  $$
  /$$$$$$$ /$$$$$$    /$$$$$$ | $$         | $$         | $$  \\ $$
 /$$_____/|_  $$_/   /$$__  $$| $$       /$$$$$$$$      | $$  | $$
| $$        | $$    | $$  \\__/| $$      |__  $$__/      | $$  | $$
| $$        | $$ /$$| $$      | $$         | $$         | $$/$$ $$
|  $$$$$$$  |  $$$$/| $$      | $$         |__/         |  $$$$$$/
 \\_______/   \\___/  |__/      |__/                       \\____ $$$
                                                              \\__/
To start hecking.

Arjun       Gowri      Jesvin      Joshua
        `}
      </pre>
    </div>
  );
}
