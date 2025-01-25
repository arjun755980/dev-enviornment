import React, { useState } from "react";
// import axios from "axios";
import CodeEditor from "./CodeEditor";
import CodeOutput from "./CodeOutput";
import "../styles/CodeWindow.css";

function CodeWindow({ filename, lang, closeCodeWindow }) {
  const [code, setCode] = useState("");
  const [output, setOutput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const runCode = async () => {
    setIsLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/execute_code", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          code: code,
          language: lang,
        }),
      });

      const data = await response.json();
      setOutput(data.output);
    } catch (error) {
      console.log(error);
      setOutput("Error running the code.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="theWindow">
      <div className="heading">
        <p className="filename">{filename}</p>
        <div>
          <button
            className="runButton"
            style={{
              fontWeight: "light",
              height: "28px",
              marginRight: "10px",
            }}
            onClick={runCode}
          >
            {isLoading ? "Walking.." : <>&#9654;</>}
          </button>
          <button
            className="runButton"
            onClick={closeCodeWindow}
            style={{
              fontWeight: "bold",
              height: "28px",
              fontSize: "16px",
            }}
          >
            &times;
          </button>
        </div>
      </div>
      <CodeEditor lang={lang} setCode={setCode} />
      <CodeOutput output={output} />
    </div>
  );
}

export default CodeWindow;
