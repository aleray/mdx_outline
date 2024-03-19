from markdown.test_tools import TestCase
from mdx_outline import OutlineExtension


class TestOutline(TestCase):
    def test_basic(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                """
                # 1
                Section 1
                ## 1.1
                Subsection 1.1
                ## 1.2
                Subsection 1.2
                ### 1.2.1
                Hey 1.2.1 Special section
                ### 1.2.2
                #### 1.2.2.1
                # 2
                Section 2
                """
            ),
            # The expected HTML output
            self.dedent(
                """
                <section class="section1"><h1>1</h1>
                <p>Section 1</p>
                <section class="section2"><h2>1.1</h2>
                <p>Subsection 1.1</p>
                </section><section class="section2"><h2>1.2</h2>
                <p>Subsection 1.2</p>
                <section class="section3"><h3>1.2.1</h3>
                <p>Hey 1.2.1 Special section</p>
                </section><section class="section3"><h3>1.2.2</h3>
                <section class="section4"><h4>1.2.2.1</h4>
                </section></section></section></section><section class="section1"><h1>2</h1>
                <p>Section 2</p>
                </section>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            extensions=[OutlineExtension()],
            output_format="html",
        )

    def test_custom_class(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                """
                # Introduction
                # Body
                ## Subsection
                # Bibliography
                """
            ),
            # The expected HTML output
            self.dedent(
                """
                <div class="s1"><h1>Introduction</h1>
                </div><div class="s1"><h1>Body</h1>
                <div class="s2"><h2>Subsection</h2>
                </div></div><div class="s1"><h1>Bibliography</h1>
                </div>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            extensions=[OutlineExtension(wrapper_tag="div", wrapper_cls="s%(LEVEL)d")],
            output_format="html",
        )


