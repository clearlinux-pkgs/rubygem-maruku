#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-maruku
Version  : 0.7.2
Release  : 6
URL      : https://rubygems.org/downloads/maruku-0.7.2.gem
Source0  : https://rubygems.org/downloads/maruku-0.7.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-maruku-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
No detailed description available

%package bin
Summary: bin components for the rubygem-maruku package.
Group: Binaries

%description bin
bin components for the rubygem-maruku package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n maruku-0.7.2
gem spec %{SOURCE0} -l --ruby > rubygem-maruku.gemspec

%build
gem build rubygem-maruku.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
maruku-0.7.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/maruku-0.7.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/MIT-LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/bin/maruku
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/bin/marutex
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/data/entities.xml
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/docs/div_syntax.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/docs/entity_test.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/docs/markdown_syntax.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/docs/maruku.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/docs/math.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/docs/other_stuff.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/docs/proposal.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/attributes.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/defaults.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/element.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/div.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/fenced_code.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/elements.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/mathml_engines/blahtex.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/mathml_engines/itex2mml.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/mathml_engines/none.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/mathml_engines/ritex.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/parsing.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/to_html.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/ext/math/to_latex.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/charsource.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/html_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/linesource.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/mdline.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/parse_block.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/parse_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input/parse_span.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/input_textile2/t2_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/inspect_element.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/maruku.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/output/entity_table.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/output/s5/fancy.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/output/s5/to_s5.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/output/to_html.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/output/to_latex.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/output/to_markdown.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/output/to_s.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/string_utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/textile2.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/toc.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/lib/maruku/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/abbrev.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/abbreviations.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/alt.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/amps.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/attribute_sanitize.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/attributes/att2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/attributes/att3.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/attributes/attributes.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/attributes/circular.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/attributes/default.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/auto_cdata.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/blank.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/blanks_in_code.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/bug_def.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/bug_table.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/code.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/code2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/code3.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/code4.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/data_loss.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/div_without_newline.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/divs/div1.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/divs/div2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/divs/div3_nest.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/easy.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/email.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/empty_cells.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/encoding/iso-8859-1.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/encoding/utf-8.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/entities.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/escape.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/escaping.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/extra_dl.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/extra_header_id.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/extra_table1.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/fenced_code_blocks.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/fenced_code_blocks_highlighted.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/footnotes.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/footnotes2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/hard.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/header_after_par.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/headers.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/hex_entities.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/hrule.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/html3.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/html4.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/html5.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/html_block_in_para.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/html_inline.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/html_trailing.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/ie.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/iframe.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/ignore_bad_header.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/images.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/images2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/inline_html.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/inline_html2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/inline_html_beginning.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue106.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue115.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue117.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue120.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue123.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue124.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue126.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue130.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue20.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue26.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue29.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue30.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue31.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue40.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue64.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue67.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue70.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue72.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue74.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue79.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue83.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue85.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue88.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue89.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/issue90.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/link.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/links.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/links2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/list1.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/list12.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/list2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/list_multipara.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists10.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists11.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists12.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists13.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists14.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists15.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists6.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists7b.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists9.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_after_paragraph.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_blank.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_blockquote_code.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_need_blank_line.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_nested.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_nested_blankline.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_nested_deep.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_ol.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_paraindent.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/lists_tab.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/loss.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math-blahtex/equations.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math-blahtex/inline.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math-blahtex/math2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math-blahtex/table.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/embedded_invalid_svg.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/embedded_svg.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/equations.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/inline.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/math2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/notmath.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/raw_mathml.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/spaces_after_inline_math.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/table.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/math/table2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/misc_sw.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/olist.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/one.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/paragraph.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/paragraph_rules/dont_merge_ref.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/paragraph_rules/tab_is_blank.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/paragraphs.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/recover/recover_links.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/ref_with_period.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/ref_with_title.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/references/long_example.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/references/spaces_and_numbers.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/smartypants.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/syntax_hl.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/table_attributes.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/table_colspan.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/tables.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/tables2.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/test.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/ticks.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/toc.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/triggering.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/underscore_in_words.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/wrapping.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/xml.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/xml3.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/xml_comments.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_docs/xml_instruction.md
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/block_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/cli_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/span_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/maruku-0.7.2/spec/to_html_utf8_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/maruku-0.7.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/maruku
/usr/bin/marutex
