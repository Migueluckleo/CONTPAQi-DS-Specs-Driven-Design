// Read-only Tab evidence reader. DATA.ids comes from the complete source inventory.
figma.skipInvisibleInstanceChildren = false;
const fields = ['id','name','type','key','remote','x','y','width','height','visible','clipsContent','opacity','blendMode','absoluteBoundingBox','absoluteRenderBounds','layoutMode','layoutWrap','layoutSizingHorizontal','layoutSizingVertical','layoutPositioning','primaryAxisSizingMode','counterAxisSizingMode','primaryAxisAlignItems','counterAxisAlignItems','itemSpacing','counterAxisSpacing','paddingTop','paddingRight','paddingBottom','paddingLeft','minWidth','maxWidth','minHeight','maxHeight','layoutGrow','layoutAlign','constraints','strokesIncludedInLayout','fills','backgrounds','strokes','strokeWeight','strokeTopWeight','strokeRightWeight','strokeBottomWeight','strokeLeftWeight','strokeAlign','dashPattern','cornerRadius','topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius','effects','isMask','maskType','boundVariables','explicitVariableModes','resolvedVariableModes','reactions','variantProperties','componentProperties','componentPropertyReferences','overrides','characters','fontName','fontSize','fontWeight','lineHeight','letterSpacing','paragraphSpacing','paragraphIndent','textAlignHorizontal','textAlignVertical','textCase','textDecoration','textAutoResize','textTruncation','maxLines','textStyleId','fillStyleId','strokeStyleId','effectStyleId','gridStyleId','layoutGrids'];
const clean = value => JSON.parse(JSON.stringify(value, (_,v) => typeof v === 'symbol' ? 'MIXED' : v));
const nodes = [], errors = [];
for (const id of DATA.ids) {
  const n = await figma.getNodeByIdAsync(id);
  if (!n) { errors.push({id,field:'identity',error:'Not found'}); continue; }
  const v = {parentId:n.parent?.id??null};
  for (const field of fields) {
    try { if (field in n && n[field] !== undefined) v[field] = clean(n[field]); }
    catch(error) { errors.push({id,field,error:String(error)}); }
  }
  v.childIds = 'children' in n ? n.children.map(c=>c.id) : [];
  if (n.type === 'COMPONENT_SET' || (n.type === 'COMPONENT' && n.parent?.type !== 'COMPONENT_SET'))
    v.componentPropertyDefinitions = clean(n.componentPropertyDefinitions);
  if (n.type === 'COMPONENT' || n.type === 'COMPONENT_SET') {
    v.description = n.description;
    v.documentationLinks = n.documentationLinks;
  }
  if (n.type === 'TEXT') {
    try { v.styledSegments = clean(n.getStyledTextSegments(['fontName','fontSize','fills','textStyleId','lineHeight','letterSpacing'])); }
    catch(error) { errors.push({id,field:'styledSegments',error:String(error)}); }
  }
  nodes.push(v);
}
return {requested:DATA.ids,nodes,errors,readOnly:true};
