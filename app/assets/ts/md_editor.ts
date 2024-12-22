import { EditorState } from "@codemirror/state";
import { markdown } from "@codemirror/lang-markdown";
import { autocompletion, closeBrackets, closeBracketsKeymap, completionKeymap } from '@codemirror/autocomplete'
import { defaultKeymap, history, historyKeymap } from '@codemirror/commands'
import { bracketMatching, defaultHighlightStyle, foldGutter, foldKeymap, syntaxHighlighting } from '@codemirror/language'
import { highlightSelectionMatches, searchKeymap } from '@codemirror/search'
import { drawSelection, dropCursor, EditorView, highlightActiveLine, highlightActiveLineGutter, highlightSpecialChars, keymap, lineNumbers, ViewUpdate } from '@codemirror/view'
import { dracula } from 'thememirror'

const editors = document.querySelectorAll('[id ^= "cm-editor-"]');
Array.prototype.forEach.call(editors, (e, i) => {
    const textarea = document.getElementById(e.id.substring(10, e.id.length)) as HTMLTextAreaElement;
    function onEditorChange(update: ViewUpdate) {
        textarea.innerHTML = update.state.doc.toString();
    }

    new EditorView({
        parent: e,
        state: EditorState.create({
            extensions: [
                lineNumbers(),
                highlightActiveLineGutter(),
                highlightSpecialChars(),
                history(),
                foldGutter(),
                drawSelection(),
                dropCursor(),
                EditorState.allowMultipleSelections.of(true),
                syntaxHighlighting(defaultHighlightStyle, { fallback: true}),
                bracketMatching(),
                closeBrackets(),
                autocompletion(),
                highlightActiveLine(),
                highlightSelectionMatches(),
                keymap.of([
                    ...closeBracketsKeymap,
                    ...defaultKeymap,
                    ...searchKeymap,
                    ...historyKeymap,
                    ...foldKeymap,
                    ...completionKeymap,
                ]),
                markdown(),
                dracula,
                EditorView.updateListener.of(onEditorChange)
            ],
        })
    });
});