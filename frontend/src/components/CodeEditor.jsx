// CodeEditor.jsx
import React, { useState } from "react";
import Editor from "@monaco-editor/react";

function CodeEditor({ lang, setCode }) {
  let initialCode = "";

  switch (lang) {
    case "python":
      initialCode = "# You may start now.";
      break;

    case "c":
      initialCode = "/* You may start now. */";
      break;

    case "javascript":
      initialCode = "/* You may start now. */";
      break;

    case "typescript":
      initialCode = "/* You may start now. */";
      break;  

    default:
      initialCode = "";
      break;
  }
  const [value, setValue] = useState(initialCode);

  const handleEditorChange = (value) => {
    setValue(value);
    setCode(value);
  };

  console.log(lang);

  return (
    <Editor
      height="60%"
      width="100%"
      defaultLanguage={lang}
      value={value}
      theme="vs-dark"
      onBlur={handleEditorChange}
      options={{
        minimap: {
          enabled: false,
        },
        overviewRulerBorder: false,
        padding: {
          bottom: 2,
          top: 2,
        },
        scrollbar: {
          verticalScrollbarSize: 20,
        },
      }}
    />
  );
}

export default CodeEditor;
